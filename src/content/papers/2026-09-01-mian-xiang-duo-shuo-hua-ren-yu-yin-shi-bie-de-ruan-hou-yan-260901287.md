---
title: Soft Posterior Speaker Injection for Multi-Talker Speech Recognition
title_zh: 面向多说话人语音识别的软后验说话人注入方法
authors:
- Jian Zhu
- Cheng Luo
affiliations:
- Zhejiang Lab
- Zhejiang International Studies University
arxiv_id: '2609.01287'
url: https://arxiv.org/abs/2609.01287
pdf_url: https://arxiv.org/pdf/2609.01287
published: '2026-09-01'
collected: '2026-09-05'
category: Other
direction: 多说话人语音识别 · 预训练模型适配
tags:
- MT-ASR
- Whisper
- FiLM
- Soft Posterior
- SOT
one_liner: 通过FiLM层与解码器说话人记忆提示向Whisper注入软说话人后验，提升重叠语音识别准确率
practical_value: '- 电商语音客服/直播字幕多说话人识别场景，可复用软后验注入思路替代硬分窗，降低重叠语音转写错误

  - 预训练大模型微调时，可借鉴「轻量预测头+FiLM层+解码器提示」的组合方案注入外部信号，降低微调成本

  - 高重叠样本占比高的场景，可复用freeze-posterior适配策略，进一步提升特定场景下的模型性能'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多说话人语音识别中，基于硬切分的级联方案易引入不可逆错误，现有SOT方案无需显式切分但未将预训练编码器与说话人活动绑定，重叠场景下词错误率高。

### 方法关键点
SPSI方案新增轻量预测头输出帧级说话人后验，通过多层FiLM层向Whisper编码器注入特征，同时在解码器侧新增说话人记忆提示，无需修改预训练模型主体结构。

### 关键结果数字
两说话人LibriSpeech重叠测试集上，cpWER从SOT的50.7%降至49.6%，高重叠区间从60.4%降至58.8%；OV-heavy场景适配后，LibriCSS 8-9会话cpWER从37.5%降至32.4%；消融实验验证编码器FiLM注入与解码器提示效果互补，软后验信号效果优于硬标签。
