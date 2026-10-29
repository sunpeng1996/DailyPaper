---
title: Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue
title_zh: 言语还是行动：LLM如何预测人机对话中的用户决策
authors:
- Baiqiao Zhang
- Shuai Ma
- Zhifeng Liao
- Chao Zhou
- Jianshu Wang
- Yuhan Zhao
- Chaoyue Zhang
- Tongjun Si
- Yuying Tang
- Xiangxian Li
affiliations:
- 香港科技大学
- 中国科学院软件研究所
- 山东大学
- 清华大学
arxiv_id: '2610.36813'
url: https://arxiv.org/abs/2610.36813
pdf_url: https://arxiv.org/pdf/2610.36813
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: Agent 人机交互用户决策预测
tags:
- User Modeling
- Human-Agent Interaction
- Decision Prediction
- LLM Evaluation
- Conversational System
one_liner: 基于人机博弈实验揭示LLM预测用户决策时过度依赖口头承诺、忽略Agent特质与上下文
practical_value: '- 对话式电商导购/客服Agent做用户成交、履约预测时，不要过度依赖用户口头承诺（如「我会下单」「我会付款」），必须结合用户历史行为（浏览、加购、过往履约记录）加权，避免给虚假承诺的用户让利造成损失

  - 多Agent服务场景（如不同风格的导购、售后Agent）不能共用统一的用户行为预测模型，需按Agent人设做分群校准：用户对亲和型Agent的履约率显著高于外向型Agent，通用模型会出现10%以上的预测偏差

  - 评估用户决策预测模型时不能只看整体AUC/准确率，必须拆分「履约/违约承诺」「不同Agent人设」「用户-Agent特质匹配度」等细维度，避免整体指标好看但高价值场景（如用户违约）误差过大

  - 引入用户特征优化预测时，优先喂结构化的「历史承诺-履约记录」，效果远优于直接喂原始人格量表分数：前者可将异常预测偏差完全修正，后者仅能降低25%左右的偏差'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前对话式Agent（电商导购、客服等）普遍基于用户对话内容预测后续决策，但在存在利益冲突的交互场景中，用户常做出虚假承诺诱导对方让利，现有LLM预测模型对口头表述、历史行为、交互Agent特征的权重分配合理性缺乏验证，整体评估指标也容易掩盖细分场景的严重误差。

### 方法关键点
- 基于Personality-1260数据集：42名用户分别与5个预设不同大五人格的GPT-4o Agent进行6轮带前置对话的重复囚徒困境博弈，每轮用户可自由对话后选择合作/背叛
- 选取Qwen3.5、Gemma4、GLM-4等8个主流开源指令微调LLM作为预测器，设置19种输入组合（仅历史决策/仅对话/混合输入），拆分履约/违约承诺、不同Agent人设、用户-Agent特质匹配度等维度评估
- 补充插入承诺语句、补充人格特征、补充历史履约记录等消融实验，验证模型对不同信息的敏感度

### 关键结果
仅用用户历史决策的预测AUC达0.80，加入对话后整体AUC无显著提升；加入对话后履约场景准确率从0.76升至0.95，违约场景准确率从0.65骤降至0.17；用户对亲和型Agent合作率达70.6%，对外向型仅54.5%，但LLM预测的两类合作率几乎无差异（64.5% vs 63.1%）；用户做出与历史行为不符的承诺时实际履约率仅40%，LLM预测的履约概率却高达69%。

### 核心结论
对话式用户决策预测不能只看整体指标，必须结合用户历史履约记录和交互Agent特征给口头承诺动态加权，否则整体准确率好看的模型会在用户违约、特定Agent交互等关键场景出现致命误差
