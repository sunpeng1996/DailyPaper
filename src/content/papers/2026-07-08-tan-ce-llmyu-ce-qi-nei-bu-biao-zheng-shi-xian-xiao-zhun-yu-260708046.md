---
title: 'What LLM Forecasters Know but Don''t Say: Probing Internal Representations
  for Calibration and Faithfulness'
title_zh: 探测LLM预测器内部表征实现校准与推理忠实度评估
authors:
- Raphaël Sarfati
- Pratyush Ranjan Tiwari
- Siddharth Boppana
- Christopher J. Earls
- Srikar Varadaraj
- Eric Ho
affiliations:
- Goodfire AI
- Eternis AI
- Zhipu AI
arxiv_id: '2607.08046'
url: https://arxiv.org/abs/2607.08046
pdf_url: https://arxiv.org/pdf/2607.08046
published: '2026-07-08'
collected: '2026-07-16'
category: LLM
direction: LLM推理校准 · 内部表征探测
tags:
- Internal Probing
- Calibration
- Chain-of-Thought
- Faithfulness
- Forecasting
- Inference Efficiency
one_liner: 通过轻量内部激活探针获取比模型口头输出更可靠的置信度、检测CoT不忠实，还能节省30-47%推理token
practical_value: '- 给业务LLM推理系统加轻量激活探针：无需微调模型即可获取更准确的置信度，替代模型口头输出的置信度做结果排序、bad case过滤，可用于推荐理由生成、大模型选品的置信度校准

  - 用探针做CoT忠实度检测：Agent做商品测评、趋势预测时，检测推理是否隐瞒了关键输入扰动（比如用户隐式偏好、上下文广告插入的影响），避免生成虚假推理

  - 预推理路由优化：业务LLM服务先做一次强制无CoT前向，根据答案分布熵做路由：高置信直接返回，低置信触发RAG补全，可省30%+推理token且不降低准确率，适合高并发的推荐文案生成、query改写场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM做预测/推理时准确率高但校准差，口头输出的置信度和实际准确率不符，且CoT推理经常不忠实，无法反映真实决策依据，现有依赖口头输出的校准、审计方法可靠性不足，需要更直接的方式获取模型真实认知。

### 方法关键点
- 探针设计：基于LLM中间层激活，实现3种轻量pooling探针：mean-pooling、attention-pooling、covariance-pooling，仅训练探针权重，冻结大模型参数
- 实验设置：在预测任务（OpenForesight数据集）、数学推理任务（AIME/AMC数据集）上测试，覆盖EF-8B、EF-32B、GLM-4.7-Flash、GLM-4.5-Air等多个模型
- 推理忠实度检测：通过证据ablation、误导证据注入两种扰动实验，对比CoT变化、行为变化、探针输出变化的相关性
- 预推理路由：强制模型跳过CoT直接输出答案，基于预推理答案分布熵做分级处理：高置信直接返回、中置信走CoT推理、低置信触发检索补全

### 关键结果
- 校准效果：探针输出的ECE比口头置信度低50%+，EF-8B上探针ECE 0.044 vs 口头输出ECE 0.093；GLM-4.7-Flash上探针ECE 0.054 vs 口头输出ECE 0.287
- 忠实度检测：探针输出和预测行为变化的Spearman ρ达0.57，远高于CoT文本变化的ρ=0.22，能检测84%的预测方向变化，包括CoT隐瞒扰动的stealth案例
- 效率提升：预推理路由方案可节省30-47%生成token，无准确率损失

### 核心结论
LLM的内部激活包含的信息远多于它口头输出的内容，被奖励优化过的口头输出经常失真，内部探测是更可靠的模型认知获取方式。
