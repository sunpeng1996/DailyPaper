---
title: 'UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI writing bypass
  state-of-the-art detectors'
title_zh: UTS ELOQUENT 2026竞赛方案：AI写作结构偏移绕过SOTA检测器
authors:
- Dima Galat
- Marian-Andrei Rizoiu
affiliations:
- University of Technology Sydney, Australia
arxiv_id: '2607.13565'
url: https://arxiv.org/abs/2607.13565
pdf_url: https://arxiv.org/pdf/2607.13565
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: LLM生成文本对抗检测攻防
tags:
- AI-text-detection
- adversarial-attack
- out-of-distribution
- evasion-attack
- adversarial-fine-tuning
one_liner: 发现AI文本检测器OOD结构偏移漏洞，提出两类攻击方案登顶2026竞赛榜单
practical_value: '- 电商AI营销文案、Agent回复需要规避平台内容检测时，可直接使用跨年代语体迁移、意识流结构改写的Prompt Trick，无需微调即可大幅提升通过率

  - 做UGC/AI生成内容合规检测时，需新增跨年代文风、非传统叙事结构等OOD样本的校验逻辑，避免漏判违规生成内容

  - 优化AI文本检测器对抗鲁棒性时，仅补充对应风格训练数据无法封堵OOD结构偏移漏洞，需额外引入分布外鲁棒性优化方案'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
经过对抗微调的SOTA AI生成文本检测器可轻松封堵2025年主流逃逸方案，亟需找到能在长期攻防对抗中存活的逃逸方法。
### 方法关键点
1. 发现检测器漏洞的不对称性：将生成文本推出检测器训练分布可稳定绕过检测，模仿人类训练分布的优化方法完全失效
2. 提出两类OOD攻击族：跨年代语体攻击（适配不同年代文本表达风格）、现代主义意识流结构攻击（调整文本叙事结构）
3. 验证常规对抗防御方案（训练数据中加入对应时期散文）无法封堵该漏洞
### 关键结果
方案包揽ELOQUENT 2026 Voight-Kampff竞赛榜单前5，逃逸率比原有方法最高提升50倍，且生成文本保留高自然度
