---
title: 'Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language
  Models on English Yoruba Code-Switched Speech'
title_zh: 超越词错误率：英-约鲁巴语码转换语音的ASR与音频LM切换感知评估
authors:
- Chibuzor Okocha
- Christan Earl Grant
affiliations:
- University of Florida
arxiv_id: '2609.11786'
url: https://arxiv.org/abs/2609.11786
pdf_url: https://arxiv.org/pdf/2609.11786
published: '2026-09-10'
collected: '2026-09-13'
category: Eval
direction: 多语言语音模型评估 · 语码切换场景
tags:
- ASR
- Audio LLM
- Code-Switching
- Evaluation Metric
- Low-Resource Language
one_liner: 提出语码转换场景切换感知评估体系，证明整体WER会掩盖模型语言切换点真实性能差异
practical_value: '- 做多语种跨境电商语音搜索、语音交互Agent时，不可仅用整体WER做验收指标，需补充切换点错误率、单语种错误率等细粒度指标，避免用户多语混说场景下性能雪崩

  - 低资源语种语音识别优化时，可重点针对语言切换进入低资源语种的窗口区域做专项微调，投入产出比更高

  - 用生成式Audio LM做语音转写时，需针对性优化prompt模板，可大幅减少翻译、冗余输出、prompt泄露等异常问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有ASR、Audio LM在单语种基准上WER表现优异，但低资源、带变音符号的多语语码转换场景下的性能缺乏细粒度评估，整体WER会掩盖大量真实问题。
### 方法关键点
构建2000条英语-约鲁巴语语码转换语音确定性评测集，对6个ASR模型、5个Audio LM做统一打分；除传统WER外，新增4类切换感知细粒度指标：切换入口token错误率（SETER）、窗口化切换点错误率、语种专属错误率、变音不敏感WER。
### 关键结果数字
1. WER最优的ASR模型与头部Audio LM的WER无统计差异，但Audio LM在所有切换相关指标上表现显著更优；
2. 所有可靠系统的约鲁巴语token识别错误率≥0.97，错误高度集中在切换进入约鲁巴语的位置；
3. 部分生成式Audio LM存在翻译、冗余输出、prompt泄露问题，且问题出现概率与prompt强相关。
