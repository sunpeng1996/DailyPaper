---
title: Complex-Text Robustness Evaluation and Failure Diagnosis for Low-Resource Multilingual
  Text-to-Speech
title_zh: 低资源多语言语音合成系统的复杂文本鲁棒性评估与故障诊断
authors:
- Tianlun Zuo
- Ziyu Zhang
- Tingzhi Mao
- Zhonghua Fu
- Lei Xie
affiliations:
- Northwestern Polytechnical University
- iFLYTEK Company Ltd. (Xi'an)
arxiv_id: '2609.11545'
url: https://arxiv.org/abs/2609.11545
pdf_url: https://arxiv.org/pdf/2609.11545
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 多语言TTS · 鲁棒性评估
tags:
- TTS
- Robustness Evaluation
- Low-Resource Language
- Multilingual
- Text Risk Score
one_liner: 面向低资源多语言TTS提出复杂文本鲁棒性诊断框架及无训练轻量化输入风险分TRS
practical_value: '- 多语言出海电商的语音播报场景（商品介绍、自动客服语音）可复用框架的三类评估维度做TTS系统效果验收，避免复杂文案生成劣质语音

  - 上线前可直接复用无训练TRS对输入文案（含数字、商品名实体、多语混排内容）做预筛查，提前拦截高风险输入

  - 针对测试暴露的TTS薄弱项（数字归一化、商品实体处理、长文案生成）优先优化，可快速提升多语言语音交互体验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有低资源多语言TTS评估多基于常规短句，仅聚焦自然度、说话人相似度等指标，无法暴露数字、日期、命名实体、长句、码-switch等复杂输入下的故障模式，鲁棒性诊断能力缺失。
### 方法关键点
1. 从内容一致性、语言一致性、生成稳定性三个维度构建鲁棒性诊断框架，针对泰、越、斯瓦希里、印尼4种低资源语言设计覆盖多类复杂文本的测试集
2. 引入Character Error Rate、语言识别准确率、时长异常率三类自动诊断指标
3. 提出无标注、无训练的轻量化Text Risk Score (TRS)，基于可解释文本特征预评估合成风险
### 关键结果
在OmniVoice、VoxCPM2、MMS-TTS三类主流多语言TTS上测试，复杂输入可暴露常规短句评估无法覆盖的系统性故障，不同系统在数字归一化、实体处理等模块各有脆弱点；TRS与内容错误、时长异常正相关，可作为低成本预合成风险指标。
