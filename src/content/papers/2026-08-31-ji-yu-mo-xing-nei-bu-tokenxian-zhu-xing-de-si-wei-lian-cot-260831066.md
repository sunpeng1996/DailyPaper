---
title: 'Every Token Leaves a Ripple in the Stream of Thought: Eliciting Model-Internal
  Token Saliency for Chain-of-Thought Compression'
title_zh: 基于模型内部Token显著性的思维链（CoT）压缩方法MIST
authors:
- Tianyi Zhao
- Yinhan He
- Wendy Zheng
- Chen Chen
affiliations:
- University of Virginia
arxiv_id: '2608.31066'
url: https://arxiv.org/abs/2608.31066
pdf_url: https://arxiv.org/pdf/2608.31066
published: '2026-08-31'
collected: '2026-09-01'
category: Reasoning
direction: 大模型推理优化 · CoT压缩
tags:
- Chain-of-Thought
- Token Pruning
- Residual Stream
- Reasoning Efficiency
- Model Saliency
one_liner: 基于模型残差流双维度显著性打分实现低精度损失的高效CoT压缩
practical_value: '- 电商/导购Agent多步推理场景可直接复用MIST框架压缩CoT路径，降低推理延迟与KV cache占用，提升服务并发量，实测精度损失远低于其他剪枝方法

  - 生成式推荐/广告文案生成场景可借鉴双维度token重要性设计，无需外部scorer即可精准定位核心信息token，避免跨模型偏差，压缩prompt长度同时保留核心语义

  - 大规模CoT微调数据预处理阶段，可复用MIST的一阶泰勒近似优化方法，仅需2次反向传播即可获得全token重要性，相比逐token前向评估成本下降一个数量级

  - LLM推理相关的token筛选任务（如query改写关键词保留、推荐理由核心信息提取）均可借鉴必要性+充足性的双维度评估框架，比单维度注意力/困惑度指标效果更稳定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Chain-of-Thought (CoT) 可大幅提升LLM多步推理效果，但过长推理链会显著升高推理延迟、显存占用与服务成本；现有token级CoT压缩方法依赖外部scorer或启发式信号，与目标模型内部计算过程弱相关，压缩后精度损失大，无法适配业务的低延迟高准确率需求。

### 方法关键点
- 定义双维度token重要性：**必要性**为移除某token残差后答案似然的下降幅度，反映全链推理对该token的依赖度；**充足性**为仅引入该token残差时答案似然的提升幅度，反映该token单独承载答案信息的能力，二者弱相关，互补覆盖不同维度的贡献。
- 采用一阶泰勒展开近似两个维度的干预效果，仅需2次反向传播即可算出所有token的重要性，复杂度不随链长增长，远低于逐token前向干预的O(T)成本，可落地大规模数据处理。
- 基于logit lens的层权重聚合多层结果，加权融合双维度得分得到最终MIST分数，按分数保留指定比例的top token生成压缩CoT，用压缩后的链做LoRA微调，使模型获得短链推理能力。

### 关键结果
在GSM8K、MATH、MMLU-Pro、BBH四个推理基准，覆盖Qwen2.5、Llama-3.1、Mistral在内的4款主流开源LLM上测试，对比TokenSkip、GoGI等9个基线方法：平均精度损失比最强基线TokenSkip低1.9pp，MATH数据集上甚至比全CoT精度高1.2~5.3pp，同时推理链长度压缩率达9.3%~21.3%。

最值得记住的一句话：与其用外部启发式规则判断token重要性，不如直接从模型自身的残差流计算过程中提取贡献信号，适配性更强、精度更高
