---
title: Incidental information contaminates patient notes and disrupts clinical reasoning
  in large language models
title_zh: 偶然信息污染临床病历并干扰大模型临床推理效果
authors:
- Krithik Vishwanath
- Brandon Ye
- Anton Alyakin
- John E. Markert
- Aaron Hsieh
- Michał Mańkowski
- Eric K. Oermann
affiliations:
- NYU Langone Health
- Johns Hopkins University School of Medicine
- Washington University School of Medicine in St. Louis
- University of Alabama at Birmingham Heersink School of Medicine
- Perelman School of Medicine at the University of Pennsylvania
arxiv_id: '2610.08585'
url: https://arxiv.org/abs/2610.08585
pdf_url: https://arxiv.org/pdf/2610.08585
published: '2026-10-05'
collected: '2026-10-11'
category: LLM
direction: 大模型鲁棒性 · 无关信息干扰防护
tags:
- LLM Robustness
- Information Contamination
- Distraction Resistance
- Safety Evaluation
- Clinical LLM
one_liner: 量化临床场景下大模型对偶然无关信息的敏感度，提出对应评估流程与防护建议
practical_value: '- 对话式导购/客服Agent、直播推荐场景，可参考该思路量化评估模型对会话闲聊、背景噪音ASR转写内容的抗干扰能力，避免无关信息污染用户画像、推荐逻辑

  - 含ASR转写输入的推荐/Agent链路，可新增无关信息识别过滤前置模块，参考文中评估范式验证过滤逻辑对核心任务的影响，平衡鲁棒性与性能

  - 业务大模型微调时可参考双编码假设，加入抗干扰训练数据时避免损伤核心推理能力，可通过消融实验定位干扰相关参数模块针对性优化'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
LLM 已广泛应用于临床病历生成、推理辅助场景，但会话/录音中混入的偶然无关信息对其效果的干扰程度未被量化，缺乏对应的上线前评估与防护标准。
### 方法关键点
基于 576 条医患对话测试前沿 LLM 对闲聊等旁支内容的敏感度；在 57 条模拟会诊录音中测试 -10dB 背景异诊语音漏入后的转写与下游生成污染情况；提出 LLM 临床推理与干扰双编码假设。
### 关键结果数字
前沿模型 35% 的生成病历会插入闲聊内容，5 分制质量分波动不超过 0.2；3.7% 的生成病历错误归因旁注内容或将其用于临床判断；背景语音漏入导致 48.2% 的转写文本被污染，4 个开源模型生成的下游病历中 5.3% 存在污染；验证了支撑临床推理的 LLM 组件同时与干扰易感性相关。
