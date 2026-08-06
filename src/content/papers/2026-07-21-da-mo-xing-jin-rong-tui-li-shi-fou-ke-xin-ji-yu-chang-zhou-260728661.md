---
title: Are the Financial Reasoning from LLMs Credible? A Real World Test over Long-Horizon
  Statements
title_zh: 大模型金融推理是否可信？基于长周期财报的真实场景测试
authors:
- Xinke Tong
- Xuanming Zhang
- Tianyi Tang
- An Yang
- Jiatu Hu
- Guojie Lin
- Zhenzhen Shi
- Lingfeng Zeng
- Boyu Yang
- Bing Zhao
affiliations:
- Alibaba Group
- Tsinghua University
arxiv_id: '2607.28661'
url: https://arxiv.org/abs/2607.28661
pdf_url: https://arxiv.org/pdf/2607.28661
published: '2026-07-21'
collected: '2026-08-06'
category: Eval
direction: 大模型评测 · 金融长上下文推理
tags:
- LLM Evaluation
- Financial Reasoning
- Long Context
- Benchmark
- Tabular Reasoning
one_liner: 推出面向未裁剪长上下文财报的推理基准FININDICES，揭示大模型金融推理两大核心瓶颈
practical_value: '- 做垂直领域Agent的结构化输出任务时，可将多指标多周期的大表生成任务拆分为单指标单周期的串行查询，降低结构瓶颈带来的推理准确率损失，该思路可直接迁移到电商运营报表生成、多维度数据核对等场景

  - 高准确率要求的垂直领域LLM落地，优先通过RAG或prompt注入明确的计算规则/公式，不要依赖模型预训练内化的领域知识，比如电商GMV、复购率、ROI等核心指标计算可直接把规则写在prompt中减少错误

  - 垂直领域小模型SFT可采用高质量结构化推理轨迹作为训练数据，既能提升无提示场景的推理准确率，也不会出现灾难性遗忘，可复用该思路训练电商业务计算、广告投放效果核算等专用小模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有金融大模型评测基准多为简化的知识类选择题、短上下文单跳QA，忽略真实工业场景中跨报表对齐、时间维度去累计、会计口径匹配等复杂需求，无法验证LLM是具备结构化推理能力还是仅做表面模式匹配，直接导致金融Agent中间数据处理环节错误率高，无法落地到数值精度要求严格的业务场景。

### 方法关键点
- 构建FININDICES基准，覆盖829家上市公司、384个金融指标、28个报告期，上下文最长达32K token，平均16K，远高于同类数据集
- 设计两类任务：单指标计算（Single-Index）和多指标多周期表格生成（Table-Index），从领域知识、时间推理、口径对齐三个维度评估能力，注入干扰项、信息缺失等对抗陷阱测试鲁棒性
- 采用全有或全无的严格评分规则，表格任务必须所有指标全对且格式符合要求才得分，避免部分得分虚高

### 关键实验
测试20+主流闭源、开源通用及金融专用LLM，核心结果：1. 无公式提示时Gemini-3.1-Pro表格任务准确率从70.7%暴跌至38.22%，暴露知识瓶颈，通用LLM缺乏内化的领域规则；2. 即使有公式提示，Gemini-3.1-Pro从单指标任务的79.61%降到表格任务的70.07%，暴露结构瓶颈，多值结构化输出会消耗推理资源导致精度下降；3. 多数垂直金融大模型表格任务准确率不足10%，传统无结构语料预训练对结构化推理提升有限；4. 基于结构化推理轨迹做SFT，无提示场景下单指标准确率提升8.54%，表格提升3.82%，且无灾难性遗忘。

最值得记住的一句话：当前LLM的结构化领域推理仍高度依赖in-context提示和低复杂度输出结构，高风险场景落地必须配套规则校验、任务拆分等容错机制。
