#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                         BANNERFORGE v1.0                                  ║
║                   Professional Banner Generator                          ║
║                                                                           ║
║                      Coded by: MANSOOR BIK KAMALI                         ║
║                         Ethical Hacking Tool                              ║
║                    For Educational Purposes Only                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import pyfiglet
from colorama import init, Fore, Back, Style
import random
import time

# Initialize colorama
init(autoreset=True)

class BannerForge:
    def __init__(self):
        self.colors = [
            Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
            Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTRED_EX,
            Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX,
            Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
        ]
        self.fonts = [
            'slant', 'standard', 'big', 'block', 'bubble', 'digital',
            'lean', 'mini', 'script', 'shadow', 'smscript', 'smshadow',
            'smslant', 'starwars', 'avatar', 'cosmic', 'doom', 'epic',
            'fuzzy', 'graffiti', 'isometric1', 'isometric2', 'isometric3',
            'isometric4', 'letters', 'moscow', 'nancyj', 'nietsche',
            'pawp', 'peaks', 'pepper', 'poison', 'rot13', 'rounded',
            'serifcap', 'short', 'slant relief', 'stampatello', 'tanka'
        ]
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Print main header"""
        print(Fore.CYAN + "╔" + "═" * 70 + "╗")
        print(Fore.CYAN + "║" + Fore.WHITE + " " * 70 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.YELLOW + "         BANNERFORGE - Professional Banner Generator" + " " * 19 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.WHITE + " " * 70 + Fore.CYAN + "║")
        print(Fore.CYAN + "╚" + "═" * 70 + "╝")
        print(Fore.MAGENTA + "╔" + "═" * 70 + "╗")
        print(Fore.MAGENTA + "║" + Fore.LIGHTBLACK_EX + "         Coded by: MANSOOR BIK KAMALI" + " " * 36 + Fore.MAGENTA + "║")
        print(Fore.MAGENTA + "╚" + "═" * 70 + "╝")
        print()
    
    def show_menu(self):
        """Display main menu"""
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "📋 MAIN MENU")
        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "1." + Fore.WHITE + " Generate Banner with Your Name")
        print(Fore.GREEN + "2." + Fore.WHITE + " Generate Random Banner")
        print(Fore.GREEN + "3." + Fore.WHITE + " Generate Banner with Custom Text")
        print(Fore.GREEN + "4." + Fore.WHITE + " Show All Available Fonts")
        print(Fore.GREEN + "5." + Fore.WHITE + " Preview Font Style")
        print(Fore.GREEN + "6." + Fore.WHITE + " Save Banner to File")
        print(Fore.GREEN + "7." + Fore.WHITE + " ASCII Art Generator")
        print(Fore.RED + "0." + Fore.WHITE + " Exit")
        print(Fore.CYAN + "═" * 50)
    
    def generate_banner(self, text, font='slant', color=None):
        """Generate banner with given text and font"""
        try:
            if color is None:
                color = random.choice(self.colors)
            
            banner = pyfiglet.figlet_format(text, font=font)
            
            # Add color to each line
            colored_banner = ""
            for line in banner.split('\n'):
                colored_banner += color + line + Fore.RESET + "\n"
            
            return colored_banner
        except:
            return None
    
    def add_footer(self):
        """Add footer with creator name"""
        footer = Fore.LIGHTBLACK_EX + "═" * 50 + "\n"
        footer += Fore.LIGHTBLACK_EX + "🔧 Created by: " + Fore.CYAN + "MANSOOR BIK KAMALI" + "\n"
        footer += Fore.LIGHTBLACK_EX + "📧 Contact: " + Fore.BLUE + "github.com/mansoor511" + "\n"
        footer += Fore.LIGHTBLACK_EX + "⚠️  " + Fore.YELLOW + "For Educational Purposes Only" + "\n"
        footer += Fore.LIGHTBLACK_EX + "═" * 50
        return footer
    
    def generate_with_name(self):
        """Generate banner with user's name"""
        print(Fore.YELLOW + "\n[+] Enter your name: " + Fore.WHITE, end="")
        name = input().strip()
        
        if not name:
            name = "HACKER"
        
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "🎨 Choose Banner Style:")
        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "1." + Fore.WHITE + " Classic (Slant)")
        print(Fore.GREEN + "2." + Fore.WHITE + " Big & Bold")
        print(Fore.GREEN + "3." + Fore.WHITE + " Hacker Style")
        print(Fore.GREEN + "4." + Fore.WHITE + " Cyber Style")
        print(Fore.GREEN + "5." + Fore.WHITE + " Minimal")
        print(Fore.GREEN + "6." + Fore.WHITE + " Random")
        
        choice = input(Fore.YELLOW + "\nChoose [1-6]: " + Fore.WHITE)
        
        font_map = {
            '1': 'slant',
            '2': 'big',
            '3': 'doom',
            '4': 'cyberlarge',
            '5': 'small',
            '6': random.choice(self.fonts)
        }
        
        font = font_map.get(choice, 'slant')
        
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "🎨 Choose Color:")
        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "1." + Fore.RED + " Red")
        print(Fore.GREEN + "2." + Fore.GREEN + " Green")
        print(Fore.GREEN + "3." + Fore.YELLOW + " Yellow")
        print(Fore.GREEN + "4." + Fore.BLUE + " Blue")
        print(Fore.GREEN + "5." + Fore.MAGENTA + " Purple")
        print(Fore.GREEN + "6." + Fore.CYAN + " Cyan")
        print(Fore.GREEN + "7." + Fore.WHITE + " White")
        print(Fore.GREEN + "8." + Fore.LIGHTYELLOW_EX + " Random")
        
        color_choice = input(Fore.YELLOW + "\nChoose [1-8]: " + Fore.WHITE)
        
        color_map = {
            '1': Fore.RED,
            '2': Fore.GREEN,
            '3': Fore.YELLOW,
            '4': Fore.BLUE,
            '5': Fore.MAGENTA,
            '6': Fore.CYAN,
            '7': Fore.WHITE,
            '8': random.choice(self.colors)
        }
        
        color = color_map.get(color_choice, Fore.CYAN)
        
        print(Fore.CYAN + "\n" + "═" * 70)
        
        # Generate and display banner
        banner = self.generate_banner(name.upper(), font, color)
        if banner:
            print(banner)
        else:
            # Fallback to default font
            banner = self.generate_banner(name.upper(), 'slant', color)
            print(banner)
        
        print(self.add_footer())
        
        # Option to save
        save = input(Fore.YELLOW + "\n💾 Save this banner to file? (y/n): " + Fore.WHITE)
        if save.lower() == 'y':
            filename = f"{name}_banner.txt"
            with open(filename, 'w') as f:
                # Remove color codes for file
                clean_banner = pyfiglet.figlet_format(name.upper(), font=font)
                f.write(clean_banner)
                f.write("\n" + "=" * 50 + "\n")
                f.write("Created by: MANSOOR BIK KAMALI\n")
                f.write("GitHub: github.com/mansoor511\n")
            print(Fore.GREEN + f"[+] Banner saved to: {filename}")
        
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def random_banner(self):
        """Generate random banner"""
        random_texts = [
            "HACKER", "CYBER", "SECURITY", "ANONYMOUS", "GHOST",
            "SHADOW", "PHANTOM", "NINJA", "WARRIOR", "LEGEND",
            "MASTER", "ZERO", "NEO", "TRINITY", "MORPHEUS"
        ]
        
        text = random.choice(random_texts)
        font = random.choice(self.fonts)
        color = random.choice(self.colors)
        
        print(Fore.CYAN + "\n" + "═" * 70)
        print(Fore.YELLOW + f"[+] Random Text: {text}")
        print(Fore.YELLOW + f"[+] Font: {font}")
        print(Fore.CYAN + "═" * 70 + "\n")
        
        banner = self.generate_banner(text, font, color)
        if banner:
            print(banner)
        
        print(self.add_footer())
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def custom_banner(self):
        """Generate banner with custom text"""
        print(Fore.YELLOW + "\n[+] Enter your custom text: " + Fore.WHITE, end="")
        text = input().strip()
        
        if not text:
            text = "CUSTOM BANNER"
        
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "🎨 Available Fonts (sample):")
        print(Fore.CYAN + "═" * 50)
        
        sample_fonts = ['slant', 'big', 'doom', 'cyberlarge', 'starwars', 'avatar']
        for i, font in enumerate(sample_fonts, 1):
            print(Fore.GREEN + f"{i}." + Fore.WHITE + f" {font}")
        
        print(Fore.GREEN + "0." + Fore.WHITE + " Show all fonts")
        
        choice = input(Fore.YELLOW + "\nChoose font [1-6 or 0]: " + Fore.WHITE)
        
        if choice == '0':
            self.show_fonts()
            font_choice = input(Fore.YELLOW + "\nEnter font name: " + Fore.WHITE)
            font = font_choice if font_choice in self.fonts else 'slant'
        else:
            font_map = {'1': 'slant', '2': 'big', '3': 'doom', '4': 'cyberlarge', '5': 'starwars', '6': 'avatar'}
            font = font_map.get(choice, 'slant')
        
        print(Fore.CYAN + "\n" + "═" * 70)
        banner = self.generate_banner(text.upper(), font, Fore.CYAN)
        if banner:
            print(banner)
        
        print(self.add_footer())
        
        save = input(Fore.YELLOW + "\n💾 Save this banner to file? (y/n): " + Fore.WHITE)
        if save.lower() == 'y':
            filename = f"custom_banner.txt"
            with open(filename, 'w') as f:
                clean_banner = pyfiglet.figlet_format(text.upper(), font=font)
                f.write(clean_banner)
            print(Fore.GREEN + f"[+] Banner saved to: {filename}")
        
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def show_fonts(self):
        """Show all available fonts"""
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "📚 Available Fonts:")
        print(Fore.CYAN + "═" * 50)
        
        for i, font in enumerate(self.fonts, 1):
            print(Fore.GREEN + f"{i:2}." + Fore.WHITE + f" {font}")
        
        print(Fore.CYAN + "═" * 50)
        print(Fore.YELLOW + f"[+] Total Fonts: {len(self.fonts)}")
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def preview_font(self):
        """Preview a specific font"""
        print(Fore.YELLOW + "\n[+] Enter font name to preview: " + Fore.WHITE, end="")
        font = input().strip()
        
        if font not in self.fonts:
            print(Fore.RED + f"[-] Font '{font}' not found!")
            input(Fore.CYAN + "\nPress Enter to continue...")
            return
        
        test_text = "ABC 123"
        print(Fore.CYAN + "\n" + "═" * 70)
        print(Fore.YELLOW + f"[+] Previewing font: {font}")
        print(Fore.CYAN + "═" * 70 + "\n")
        
        banner = self.generate_banner(test_text, font, Fore.CYAN)
        if banner:
            print(banner)
        
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def ascii_art(self):
        """Simple ASCII art generator"""
        print(Fore.YELLOW + "\n[+] Enter text for ASCII art: " + Fore.WHITE, end="")
        text = input().strip()
        
        if not text:
            text = "ART"
        
        arts = [
            "╔══════╗\n║ ART ║\n╚══════╝",
            "▄▄▄▄▄▄▄▄▄▄▄\n█ ART █\n▀▀▀▀▀▀▀▀▀▀▀",
            "┌──────┐\n│ ART │\n└──────┘"
        ]
        
        print(Fore.CYAN + "\n" + "═" * 70)
        print(random.choice(arts).replace("ART", text.upper()))
        print(self.add_footer())
        
        input(Fore.CYAN + "\nPress Enter to continue...")
    
    def main(self):
        """Main execution"""
        while True:
            self.clear_screen()
            self.print_header()
            self.show_menu()
            
            choice = input(Fore.YELLOW + "\n👉 Select an option [0-7]: " + Fore.WHITE)
            
            if choice == '1':
                self.generate_with_name()
            elif choice == '2':
                self.random_banner()
            elif choice == '3':
                self.custom_banner()
            elif choice == '4':
                self.show_fonts()
            elif choice == '5':
                self.preview_font()
            elif choice == '6':
                self.custom_banner()  # Save option included inside
            elif choice == '7':
                self.ascii_art()
            elif choice == '0':
                print(Fore.GREEN + "\n[+] Thanks for using BannerForge!")
                print(Fore.CYAN + "[+] Coded by: MANSOOR BIK KAMALI")
                sys.exit(0)
            else:
                print(Fore.RED + "[-] Invalid option!")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = BannerForge()
        tool.main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Exiting...")
        sys.exit(0)
