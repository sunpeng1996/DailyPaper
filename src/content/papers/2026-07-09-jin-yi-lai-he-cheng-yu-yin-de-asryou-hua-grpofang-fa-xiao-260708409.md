---
title: 'When Synthetic Speech Is All You Have: Better Call GRPO'
title_zh: 仅依赖合成语音的ASR优化：GRPO方法效果远超SFT
authors:
- Shashi Kumar
- Yanis Labrak
- Hasindri Watawana
- Sergio Burdisso
- Esaú Villatoro-Tello
- Kadri Hacioğlu
- Petr Motlicek
- Andreas Stolcke
affiliations:
- Idiap Research Institute
- EPFL
- Uniphore
- Brno University of Technology
arxiv_id: '2607.08409'
url: https://arxiv.org/abs/2607.08409
pdf_url: https://arxiv.org/pdf/2607.08409
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 低资源ASR训练 · GRPO强化学习域适配
tags:
- GRPO
- Reinforcement Learning
- Synthetic Speech
- Domain Adaptation
- Automatic Speech Recognition
one_liner: 用无critic的GRPO强化学习基于合成语音适配ASR，相对SFT最高降45%WER
practical_value: '- 电商语音客服、合规性强的语音类业务场景无法采集真实标注数据时，可先用TTS生成合成数据，采用GRPO替代纯SFT做模型适配，大幅降低识别错误率

  - 域适配任务可复用SFT+GRPO两阶段流程：先通过SFT做初步对齐，再用RL做策略优化，比单一方法效果提升更显著

  - 序列生成类任务（ASR、query改写、文案生成等）做RL优化时，可选择无critic的GRPO方法降低工程实现复杂度，同时减少插入错误、提升序列对齐效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
受GDPR等隐私法规约束，银行、电商客服等受监管领域的真实语音数据采集成本高、合规难度大，基于合成TTS语音做ASR域适配时，传统SFT方法无法解决合成语音与真实语音声学不匹配问题，效果瓶颈明显。

### 方法关键点
摒弃传统SFT路线，采用无critic的GRPO强化学习方法，以低WER为奖励目标，仅基于合成语音做ASR模型适配，优化时保留模型底层表征不变，重点调整停止校准、注意力对齐等行为层面逻辑。

### 关键结果
- 仅用合成语音+GRPO适配，相对SFT降低40%相对WER（从36.71%降至22.09%）
- SFT预训练后再叠加GRPO优化，相对SFT的WER降低幅度进一步提升至45%
- 增益全部来自行为层面优化：插入错误显著减少、语音文本对齐更准确，模型底层表征无明显变化
