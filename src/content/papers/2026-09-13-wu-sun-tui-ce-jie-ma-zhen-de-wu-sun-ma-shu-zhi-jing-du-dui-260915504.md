---
title: How Lossless Is Lossless Speculative Decoding? The Role of Numerical Precision
  in Orthrus
title_zh: 无损推测解码真的无损吗？数值精度对Orthrus架构的影响分析
authors:
- Ilya Koziev
- Leonid Sinev
- Ivan Oseledets
arxiv_id: '2609.15504'
url: https://arxiv.org/abs/2609.15504
pdf_url: https://arxiv.org/pdf/2609.15504
published: '2026-09-13'
collected: '2026-09-15'
category: LLM
direction: LLM推理加速 · 数值精度影响评估
tags:
- Speculative Decoding
- Orthrus
- Numerical Precision
- LLM Inference
- BF16
one_liner: 验证Orthrus无损推测解码的精度依赖，BF16下轨迹匹配率仅45%，FP32下可达100%
practical_value: '- 部署Orthrus这类“无损”推测解码加速方案时，若业务要求输出严格与原生AR模型一致（如合规话术、商品参数描述生成），必须使用FP32精度推理；BF16仅适合对输出容忍度高、优先追求推理速度的场景（如推荐文案、通用客服应答）

  - 训练Orthrus的扩散分支时，采用冻结AR模型自身greedy解码生成的on-policy蒸馏数据，比通用人类语料可获得更高的Tokens Per Forward(TPF)，可直接复用该训练数据构造方法

  - 评估LLM推理加速方案的一致性时，不能仅参考下游任务benchmark得分，需额外增加轨迹级匹配验证，避免数值精度带来的输出漂移影响敏感业务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Orthrus作为融合自回归(AR)与扩散的混合推测解码架构，官方宣称可实现无损推理加速、输出与原生AR模型完全一致，但工业部署普遍采用低精度推理，其无损性是否受数值精度影响尚未得到系统验证，且现有评估多依赖下游任务benchmark，缺乏轨迹级一致性的校验逻辑。
### 方法关键点
- 独立复现Orthrus的训练与推理流程，构造on-policy蒸馏数据集：用冻结的Qwen3-1.7B模型greedy解码生成411万条prompt-response对，作为扩散分支的训练数据
- 采用双维度评估体系：一是轨迹级匹配率（与原生AR模型输出token序列的完全一致性），二是lm-eval-harness下游任务得分
- 控制变量对比BF16、FP32两种推理精度下的表现，引入响应条件困惑度分析轨迹漂移的关联因素
### 关键结果
基于12个领域共1190条prompt测试，对比原生Qwen3-1.7B、官方Orthrus checkpoint、自研训练的Orthrus模型：
1. BF16推理下，官方Orthrus轨迹匹配率仅45%，自研训练版为43%，匹配率与响应条件困惑度强负相关，困惑度越高匹配概率越低
2. BF16下的轨迹漂移未带来下游任务得分下降，GSM8K、IFEval等部分benchmark得分甚至略高于原生AR模型
3. FP32推理下，两个版本Orthrus的轨迹匹配率均达到100%，完全符合无损要求
### 核心结论
声称“无损”的LLM推理加速方案的实际无损性严格依赖数值精度，轨迹级一致性和下游任务benchmark表现是两个完全独立的评估维度，不可互相替代。
