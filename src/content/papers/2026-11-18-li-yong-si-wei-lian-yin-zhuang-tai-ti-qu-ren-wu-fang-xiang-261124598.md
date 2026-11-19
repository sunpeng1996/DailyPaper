---
title: Chain-of-Thought Hidden States Reveal Task-Solving Directions for Direct Answers
title_zh: 利用思维链隐状态提取任务方向提升大模型直接回答性能
authors:
- Houman Mehrafarin
- Ioannis Konstas
affiliations:
- Heriot-Watt University
- University of Edinburgh
arxiv_id: '2611.24598'
url: https://arxiv.org/abs/2611.24598
pdf_url: https://arxiv.org/pdf/2611.24598
published: '2026-11-18'
collected: '2026-11-19'
category: Reasoning
direction: LLM推理优化 · 隐状态操控
tags:
- Chain-of-Thought
- Hidden State
- Activation Steering
- LLM Reasoning
- Representation Engineering
one_liner: 从CoT隐状态提取问题专属任务求解方向，以1/10的推理token量获得超过CoT的准确率
practical_value: '- 电商实时导购、客服Agent场景可复用该方法：对需要多步推理的问题（如满减计算、商品搭配校验），不用生成完整CoT，将直接回答prompt的最后隐状态对齐预构建的任务方向，响应速度提升10倍，准确率超过原生CoT

  - 搜索Query意图推理、属性识别场景可借鉴正负隐状态对比思路：对每个Query类别的CoT隐状态做有效/无效推理的分组，构建类别级方向模板，对齐后直接输出结果，降低推理算力成本

  - 工程上优先采用SLERP球面线性插值做隐状态操控：相比加法式activation steering不改变隐状态范数，避免生成质量退化，可直接集成到现有LLM推理服务中做轻量化优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
CoT prompting虽能提升LLM推理准确率，但存在两大痛点：部分任务上准确率反而低于直接回答，且需生成上百token的推理过程，延迟高、算力成本高。已有研究证实CoT生成错误答案时，正确信息依然存在于其隐状态中，但尚未有方法高效利用该信息替代完整CoT生成。
### 方法关键点
- 通过激活补丁实验标注CoT隐状态：将每个CoT token的隐状态替换到直接回答prompt的最后隐层位置，能输出正确答案的标记为recovering，否则为failed；
- 训练线性探针验证两类隐状态可线性区分，同类型推理任务的探针可跨任务迁移；
- 对每个问题构造专属任务方向：取该问题所有recovering隐状态均值c+、failed隐状态均值c-，构造方向d∝c+ - 0.5c-，用SLERP将直接回答prompt的最后隐状态旋转到d方向，保持范数不变后生成答案。
### 关键结果
在25个涵盖算术、逻辑、时空、推荐等6类推理任务上测试，基线为原生CoT、直接回答prompt：
- LLaMA 3.1 8B：直接回答准确率46%，CoT 69%，本文方法达85%，平均生成19token，仅为CoT的1/10；
- Qwen 2.5 7B：直接回答准确率52%，CoT 77%，本文方法达86%，平均生成19token，仅为CoT的1/12；
- 对CoT表现劣于直接回答的任务（如电影推荐），本文方法仍可提升22~36个点的准确率。
### 核心结论
CoT不是获取高推理准确率的最短路径，每个问题的直接回答prompt表征空间中存在专属的任务求解方向，对齐后可同时实现准确率提升与推理成本下降。
