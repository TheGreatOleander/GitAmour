#!/usr/bin/env python3
"""
GITAMOUR - Where commits lead to commitment 💘
Now featuring FOSTER MODE 🧸
"""

import subprocess
import random
import os
from datetime import datetime


class HackerProfile:
    def __init__(self, username, repo_path):
        self.username = username
        self.repo_path = repo_path
        self.attractiveness_score = 0
        self.personality = {}
        self.looking_for = []
        self.red_flags = []
        self.green_flags = []

    def analyze_repo(self):
        print(f"\n💝 Analyzing {self.username}'s repository for romantic compatibility...")

        self.personality['passion'] = self._measure_commit_passion()
        self.personality['style'] = self._detect_code_personality()
        self.personality['relationship_style'] = self._analyze_branches()
        self.personality['conflict_resolution'] = self._analyze_merges()
        self.personality['communication'] = self._rate_readme()
        self.personality['responsibility'] = self._check_tests()

        self._calculate_attractiveness()
        return self

    def _run_git(self, args):
        try:
            result = subprocess.run(
                ['git'] + args,
                capture_output=True,
                text=True,
                cwd=self.repo_path
            )
            return result.stdout.strip()
        except Exception:
            return ""

    def _measure_commit_passion(self):
        output = self._run_git(['log', '--pretty=format:%ai|%s', '-100'])
        if not output:
            return 0

        commits = output.split('\n')
        late_night = sum(1 for c in commits if any(h in c for h in [' 23:', ' 00:', ' 01:', ' 02:']))
        excitement = sum(1 for c in commits if '!' in c)

        score = min((late_night * 2 + excitement) / 10, 10)

        if score > 7:
            self.green_flags.append("🔥 Commits at 2am (dedicated!)")

        return score

    def _detect_code_personality(self):
        output = self._run_git(['ls-files'])
        if not output:
            return []

        files = output.split('\n')
        extensions = set(f.split('.')[-1] for f in files if '.' in f)

        styles = []

        if len(extensions) > 5:
            styles.append('polyglot')
            self.green_flags.append("🌈 Speaks many languages")

        if 'rs' in extensions:
            styles.append('safety-conscious')
            self.green_flags.append("🦀 Memory safe (Rust)")

        if 'js' in extensions and 'ts' in extensions:
            styles.append('evolving')

        if 'sh' in extensions:
            styles.append('minimalist')

        return styles

    def _analyze_branches(self):
        output = self._run_git(['branch', '-a'])
        branches = output.split('\n') if output else []

        if len(branches) > 20:
            self.red_flags.append("⚠️ Commitment issues (20+ branches)")
            return "commitment-phobic"
        elif len(branches) > 5:
            self.green_flags.append("🌿 Healthy boundaries")
            return "balanced"
        else:
            return "monogamous"

    def _analyze_merges(self):
        output = self._run_git(['log', '--merges', '--pretty=format:%s', '-20'])
        merges = output.split('\n') if output else []

        force_merges = sum(1 for m in merges if 'force' in m.lower())
        if force_merges > 3:
            self.red_flags.append("🚩 Force merges history")
            return "aggressive"

        clean_merges = sum(1 for m in merges if 'merge' in m.lower() and 'conflict' not in m.lower())
        if clean_merges > 5:
            self.green_flags.append("✨ Clean merge history")
            return "diplomatic"

        return "avoidant"

    def _rate_readme(self):
        readme_files = ['README.md', 'README.txt', 'README']
        content = ""

        for r in readme_files:
            path = os.path.join(self.repo_path, r)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                break

        if not content:
            self.red_flags.append("📝 No README")
            return 0

        score = min(len(content) / 100, 10)

        if '❤️' in content or '💖' in content:
            self.green_flags.append("💕 Uses heart emoji")

        if len(content) > 1000:
            self.green_flags.append("📚 Detailed README")

        return score

    def _check_tests(self):
        output = self._run_git(['ls-files'])
        if not output:
            return 0

        files = output.split('\n')
        tests = [f for f in files if 'test' in f.lower() or 'spec' in f.lower()]

        if len(tests) > 5:
            self.green_flags.append("✅ Well tested")
            return 10
        elif tests:
            return 6
        else:
            self.red_flags.append("⚠️ No tests")
            return 2

    def _calculate_attractiveness(self):
        numeric_traits = [
            self.personality.get('passion', 0),
            self.personality.get('communication', 0),
            self.personality.get('responsibility', 0)
        ]

        base = sum(numeric_traits) / len(numeric_traits) if numeric_traits else 0
        base += len(self.green_flags) * 0.5
        base -= len(self.red_flags) * 0.8

        self.attractiveness_score = max(0, min(10, base))

    def nurturer_index(self):
        score = 0

        if self.personality.get('responsibility', 0) > 7:
            score += 3
        if self.personality.get('conflict_resolution') == 'diplomatic':
            score += 3
        if self.personality.get('communication', 0) > 7:
            score += 2
        if 'polyglot' in self.personality.get('style', []):
            score += 2

        return score

    def get_profile_card(self):
        hotness = '🔥' * int(self.attractiveness_score / 2)

        card = f"""
╔══════════════════════════════════════════════════════════╗
║  💘 GITAMOUR PROFILE                                     ║
╠══════════════════════════════════════════════════════════╣
║  👤 {self.username:<52}║
║  {hotness:<52}║
║                                                          ║
║  📊 ATTRACTIVENESS: {self.attractiveness_score:.1f}/10                               ║
║                                                          ║
║  🎭 PERSONALITY                                          ║
║    Passion: {self.personality.get('passion', 0):.1f}/10                               ║
║    Communication: {self.personality.get('communication', 0):.1f}/10                        ║
║    Responsibility: {self.personality.get('responsibility', 0):.1f}/10                       ║
║                                                          ║
║  🧸 Nurturer Index: {self.nurturer_index()}/10                                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
        return card


class GitAmour:
    def __init__(self):
        self.profiles = []

    def register(self, username, repo_path):
        profile = HackerProfile(username, repo_path).analyze_repo()
        self.profiles.append(profile)
        return profile

    def foster_needy_repos(self):
        needy = []

        for profile in self.profiles:
            if profile.personality.get('communication', 0) < 3:
                needy.append((profile, "📭 No README – scared to open up"))
            elif profile.personality.get('responsibility', 0) < 4:
                needy.append((profile, "🧪 No tests – never been supported"))
            elif profile.personality.get('passion', 0) < 2:
                needy.append((profile, "💤 Few commits – lost motivation"))
            elif len(profile.red_flags) > 2:
                needy.append((profile, "🚩 Complicated history – needs patience"))

        return needy


if __name__ == "__main__":
    print
