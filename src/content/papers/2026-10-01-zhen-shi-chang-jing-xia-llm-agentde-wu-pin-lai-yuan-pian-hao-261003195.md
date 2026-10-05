---
title: 'Source Preference in the Wild: How LLM Agents Favor Items by Source, and How
  to Reduce It'
title_zh: 真实场景下LLM Agent的物品来源偏好机制与缓解方法
authors:
- Jonghyun Song
- Haewon Park
- Jeonghoon Shim
- Woojung Song
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
arxiv_id: '2610.03195'
url: https://arxiv.org/abs/2610.03195
pdf_url: https://arxiv.org/pdf/2610.03195
published: '2026-10-01'
collected: '2026-10-05'
category: Agent
direction: Agent 搜索推荐来源偏见优化
tags:
- LLM Agent
- Source Preference
- Recommendation Bias
- Bias Mitigation
- DPO
one_liner: 在12款LLM Agent与3个搜索场景下验证来源偏好并给出低成本缓解方案
practical_value: '- 做Agent导购/比价场景时，优先补全所有候选商品对应用户要求的字段信息，缺失信息会触发Agent的来源刻板印象，大幅降低推荐公平性

  - 用DPO微调Agent推荐逻辑时，需平衡不同来源的正样本占比，避免模型学到来源和优质商品的虚假关联，强化来源偏见

  - 线上发现Agent有明显来源偏好时，可在系统提示词中明确告知用户关注维度（如价格、质量）与来源无关，或反向修正刻板印象，最多可降低22.5pp的偏好

  - 评估LLM4Rec/Agent推荐效果时，需加入来源公平性指标，避免偏好长期积累形成马太效应，导致优质中小商家商品被过滤'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent越来越多被用于商品、酒店、学术文献的搜索推荐决策，现有研究仅在受控实验中发现来源偏好存在，但未在真实端到端搜索场景下验证其影响机制；来源偏好会导致满足用户需求的优质商品因来源被过滤，长期会形成马太效应，同时损害用户体验和中小商家利益。

### 方法关键点
- 覆盖12款主流LLM Agent（含GPT、Gemini、Llama、Qwen、GLM、DeepSeek等），在购物、酒店、学术搜索3个真实场景共4822条用户请求下开展端到端实验
- 设计匹配对比框架：控制商品满足的用户需求数量、展示位置两个变量，用带平局修正的Bradley-Terry模型计算每个来源的偏好得分，划分为偏好/中性/厌恶三类
- 从训练关联、推理信息缺失两个维度分析成因，验证训练侧数据平衡、推理侧信息补全/提示词修正两类缓解方案的效果

### 关键结果
所有模型在三个场景均存在稳定且跨模型一致的来源偏好：偏好来源的少满足1项需求的商品，对比厌恶来源的多满足1项需求的商品，选中率中位数达68%，反向情况仅为2%；隐藏URL等来源信息可缩小偏好与厌恶来源的得分差约12pp，相同内容贴偏好来源标签后选中率最高提升64.7pp；训练侧用平衡样本的DPO微调可将原有来源偏好从60%左右降至接近50%，推理侧补全缺失信息最多降低28.3pp的偏好。

**最值得记住的一句话**：LLM Agent的来源偏好本质是训练数据关联和推理时信息缺失共同导致的捷径学习，无需大改模型即可通过数据平衡、信息补全、提示词修正三类低成本方案有效缓解。
