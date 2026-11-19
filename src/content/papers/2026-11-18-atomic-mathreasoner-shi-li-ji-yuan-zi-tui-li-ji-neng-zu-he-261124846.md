---
title: 'Atomic MathReasoner: Instance-Level Composition of Atomic Reasoning Skills
  for Mathematical LLMs'
title_zh: Atomic MathReasoner：实例级原子推理技能组合的数学LLM优化框架
authors:
- Jiashu Li
- Tianyu Gao
- Qinglong Liu
- Jinping Wang
- Ye Wei
- Zhiqiang Gao
arxiv_id: '2611.24846'
url: https://arxiv.org/abs/2611.24846
pdf_url: https://arxiv.org/pdf/2611.24846
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM数学推理 · LoRA专家组合路由
tags:
- LoRA
- Mathematical Reasoning
- Expert Routing
- Parameter Efficient Fine-tuning
- Mixture of Experts
one_liner: 通过原子LoRA专家组合原型与轻量路由实现实例级推理技能动态组合，提升数学LLM性能
practical_value: '- 可复用「分技能训练LoRA专家+离线搜索最优组合原型+轻量路由」架构，解决推荐/Agent场景多任务适配问题，避免单模型多任务能力冲突

  - 可借鉴伪标签生成的margin过滤策略，提升路由分类器训练数据质量，降低噪声对路由效果的影响

  - 小样本训练轻量路由（仅需数百样本达最优效果）的思路可复用在流量切分、个性化模型调度等业务场景，降低推理开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有数学LLM优化大多将推理视为单一整体能力，即便已有工作将数学推理拆解为原子技能，也缺乏高效的实例级技能组合机制，无法针对不同问题动态适配最优能力组合：静态全局组合易引入无关噪声，在线动态组合则会带来过高推理延迟。

### 方法关键点
- 为每个原子推理技能训练独立的LoRA专家，实现能力完全解耦
- 对验证集执行多次无梯度优化，搜索不同数据子集下的低损失LoRA组合系数，构建多样化组合原型库
- 以参考解的token级NLL为指标为样本分配最优原型伪标签，通过NLL差值margin过滤模糊样本，仅用TF-IDF特征+多分类逻辑回归训练轻量路由，无额外推理负担
- 推理时路由直接为每个问题匹配最优原型，线性组合LoRA专家参数生成答案

### 关键实验
在AtomicMath、GSM8K、MATH数据集验证，覆盖通用LLM（Llama3-8B）和数学专用LLM（InternLM2-Math-7B、Qwen2.5-Math-7B）：Qwen2.5-Math-7B加持AMR后，Level1领域平均准确率从64.4%升至68.1%，Level2从59.3%升至63.7%，逻辑推理平均得分从39.4%升至46.8%，部分任务精度超过GPT-4o、Claude 3.7 Sonnet；对比DPO、Step-DPO等优化方案，在GSM8K上精度提升3.7pp，MATH上提升3.2pp，效果优于现有方案，推理速度比动态在线组合快2.76倍。

### 核心结论
针对复杂任务的能力解耦后，仅需离线构建组合原型+轻量路由，就能以极低开销实现实例级的能力动态适配，效果显著优于全局静态组合方案。
