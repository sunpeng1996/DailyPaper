---
title: 'TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space
  Optimization'
title_zh: TextReg：基于正则化文本空间优化缓解prompt分布过拟合
authors:
- Lucheng Fu
- Ye Yu
- Yiyang Wang
- Yiqiao Jin
- Haibo Jin
- B. Aditya Prakash
- Haohan Wang
affiliations:
- Georgia Institute of Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2605.21318'
url: https://arxiv.org/abs/2605.21318
pdf_url: https://arxiv.org/pdf/2605.21318
published: '2026-10-04'
collected: '2026-10-06'
category: LLM
direction: LLM 提示优化 · 分布过拟合缓解
tags:
- Prompt Optimization
- Regularization
- OOD Generalization
- Text Gradient
- Distributional Overfitting
one_liner: 提出三阶段正则化框架TextReg，缓解prompt优化的分布过拟合，提升OOD泛化能力
practical_value: '- 做Agent/生成式推荐的自动prompt优化时，可复用Dual-Evidence Gradient Purification逻辑，过滤仅适配训练样本的特化规则，只保留通用规则，避免优化出的prompt在真实业务分布下效果滑坡

  - 业务prompt迭代时可引入Semantic Edit Regularization的双维度检测：一方面限制prompt长度膨胀节省context预算、降低KV
  cache开销，一方面检测新增规则是否为窄范围补丁，平衡迭代收益和泛化性

  - 文本梯度优化场景下，可参考TextReg的任务优先逻辑：正则化只约束prompt改写形式，不压制必要的任务性能相关更新，避免正则化导致拟合效果下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于LLM反馈的自动prompt优化方法，迭代后生成的prompt往往长度膨胀、累积大量样本特化的窄范围规则，在训练分布外的OOD场景泛化性极差，即prompt分布过拟合问题。现有方法缺乏对离散文本空间优化的表征控制，导致优化后的prompt无法直接落地到存在分布漂移的真实业务场景。

### 方法关键点
1. 定义**表征低效度**指标，将prompt低效拆分为耦合的两个维度：容量成本（prompt长度带来的context预算消耗）、范围狭窄度（规则仅适配少量样本的程度），将分布过拟合归因于两者的同步增长
2. 三阶段正则化优化流程：
   - Dual-Evidence Gradient Purification：结合本地批次证据和全局RuleBank复发证据，过滤样本特化补丁、纯风格类更新，仅保留通用规则对应的任务梯度
   - Semantic Edit Regularization：检测prompt更新后的长度变化、语义范围变化，生成对应的文本正则化梯度
   - Regularization-Guided Prompt Update：优先保证任务更新的正确性，仅用正则化梯度约束改写形式，不压制必要的性能相关更新

### 关键实验
在BBH符号推理、GSM8K算术推理等9个数据集上测试，跨Qwen2-7B、Llama3系列、Phi-3.5等4个测试LLM，对比CoT、TextGrad、REVOLVE基线，OOD精度最高较TextGrad提升11.8%、较REVOLVE提升16.5%；三个核心组件缺一不可，且优化链路的LLM替换为轻量化模型后性能下降幅度极小。

### 核心结论
prompt分布过拟合本质是表征效率问题，而非单纯的优化动力学产物，平衡任务拟合和表征效率才能得到泛化性强的优化prompt
