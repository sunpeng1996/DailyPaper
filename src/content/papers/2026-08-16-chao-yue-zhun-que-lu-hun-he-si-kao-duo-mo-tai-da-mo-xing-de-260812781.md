---
title: 'Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking
  MLLMs'
title_zh: 超越准确率：混合思考多模态大模型的响应行为基准与对齐
authors:
- Xinming Wang
- Weinong Wang
- Hongming Yang
- Yansong Lin
- Zheng Ruan
- Shangpin Peng
- Qiming Peng
- Nan Qiao
- Fengyuan Lu
- Guoqing Ma
affiliations:
- Institute of Automation, CAS
- Tencent
- University of Electronic Science and Technology of China
- Hong Kong University of Science and Technology
- Zhongguancun Academy
arxiv_id: '2608.12781'
url: https://arxiv.org/abs/2608.12781
pdf_url: https://arxiv.org/pdf/2608.12781
published: '2026-08-16'
collected: '2026-08-24'
category: Training
direction: 大模型对齐 · 混合推理模式优化
tags:
- MLLM
- Hybrid-Thinking
- Response Alignment
- RLHF
- Benchmark
one_liner: 构建响应模式诊断基准与RL对齐框架，缓解混合思考MLLM跨模式的响应行为偏差
practical_value: '- 搭建Agent多模式响应质检体系时，可复用4类响应故障（CoT泄露/重复/逻辑矛盾/表演式推理）的定义，快速落地业务侧响应质量检测规则，比如电商客服Agent的非思考模式禁止泄露内部推理过程

  - 多模态大模型RL训练时，可参考PatternRL的加权惩罚设计，在正确性奖励之外添加低权重的响应模式惩罚，既保证任务效果又避免异常输出，比如商品图文问答模型的回复不会出现冗余重复内容

  - 业务侧大模型效果评估不要只看准确率，可新增响应模式对齐度指标，尤其是混合推理模式部署的场景，比如推荐理由生成的思考/非思考模式输出风格要统一，避免用户感知差异

  - 小模型对齐时要权衡响应模式约束和效果下降问题，4B规模模型加模式惩罚后准确率掉点更明显，8B以上模型影响更小，业务部署时可根据参数规模调整惩罚权重'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前混合思考多模态大模型（MLLM）同时暴露高算力思考模式和低延迟非思考模式接口，仅靠准确率无法完整衡量响应质量：非思考模式常出现推理过程泄露、重复输出、逻辑矛盾等用户可见问题，两类模式的响应行为差异大，传统评估体系无法识别这类故障，可能直接损害用户体验。
### 方法关键点
- 构建PatternEval诊断基准：包含2415个多模态prompt，覆盖视觉感知与定位、结构化图像理解、多模态知识推理3大类任务，定向检测4类响应故障：Chain-of-Thought泄露、响应重复、逻辑矛盾、表演式推理
- 训练PatternRM奖励模型：基于Qwen3.5-27B微调，采用纯文本输入即可预测4类故障，平衡检测效果与推理效率，适合RL训练时批量调用
- 提出PatternRL对齐方案：RL训练时在正确性核心奖励之外添加模式惩罚，CoT泄露/重复惩罚权重设为0.05，逻辑矛盾/表演式推理权重设为0.02，惩罚上限为0.1，不覆盖正确性目标
### 关键结果
- 测试25款主流MLLM，非思考模式的故障触发率平均比思考模式高20pct以上，最高差距达48.64pct，推理类任务故障率显著高于感知类任务
- 相比仅优化正确性的BaseRL，PatternRL在Qwen3-VL-4B/8B上分别将非思考模式故障触发率降低13.08/14.35pct，整体准确率波动小于1pct
> 值得记住：可控的推理算力开销，不应该以不稳定的用户可见响应行为为代价
