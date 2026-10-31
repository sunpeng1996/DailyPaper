---
title: 'From Speech Tokens to Stolen Voices: Attacker-Chosen-Text Speaker Impersonation
  via Representation Inversion'
title_zh: 语音Token到被盗人声：基于表征反转的指定文本说话人冒充攻击
authors:
- Ye Lu
- Shen Wang
- Runze Liu
- Zhitao Ou
- Haonan Huang
- Yihan Yan
- Fanghui Sun
- Zhaoyang Zhang
affiliations:
- School of Cyberspace Science, Harbin Institute of Technology
arxiv_id: '2610.34688'
url: https://arxiv.org/abs/2610.34688
pdf_url: https://arxiv.org/pdf/2610.34688
published: '2026-10-26'
collected: '2026-10-31'
category: Other
direction: 语音大模型隐私安全 · 表征反转攻击
tags:
- speech_privacy
- model_inversion_attack
- speaker_impersonation
- speech_LLM
- representation_security
one_liner: 提出STIA攻击方法，仅需泄漏的短语音表征即可生成指定文本的受害者音色伪造语音
practical_value: '- 语音交互类电商Agent（如语音导购、智能语音客服）需对传输的语音表征做脱敏处理，避免用户声纹泄漏被用于诈骗等黑产行为

  - 语音类服务前后端交互协议设计时，避免直接传输原始语音表征，可添加扰动或仅传输ASR后文本+不含声纹特征的低维语义向量

  - 个性化语音生成类业务（如数字人语音、用户专属语音回复）可复用其条件流匹配语音生成框架，实现少样本指定音色语音生成'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
端到端语音大模型应用中，端侧语音前端通常将语音表征上传至云端推理，原始音频留存本地，但现有表征仍包含可复用的说话人身份信息，存在声纹泄漏、被用于伪造语音的隐私风险。

### 方法关键点
1. STIA攻击框架支持将离散、连续或混合类型的语音表征转换为条件序列；
2. 基于公开语音数据集内同说话人不同发音对训练条件流匹配语音生成模型，无需访问受害者原始音频或转录文本，仅需单条短泄漏表征即可结合攻击者指定文本生成对应受害者音色的语音。

### 关键结果
基于3秒Moshi语音表征泄漏场景，STIA生成语音的CAM++说话人余弦相似度达0.78，目标文本词错误率仅3.80%，验证了语音前端表征存在严重声纹泄漏风险。
