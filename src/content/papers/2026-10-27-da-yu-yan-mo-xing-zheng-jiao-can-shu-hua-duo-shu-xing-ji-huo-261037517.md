---
title: Orthogonal and Parametrized Multi-Attribute Steering of LLMs
title_zh: 大语言模型正交参数化多属性激活控制方法
authors:
- Remy Ogasawara
- Cullen Anderson
- Narmeen Fatimah Oozeer
- Foad Namjoo
- Amir Abdullah
- Jens Kristian Refsgaard Schou
- Jeff M. Phillips
affiliations:
- University of Utah
- University of Massachusetts Amherst
- Martian AI
- Thoughtworks
arxiv_id: '2610.37517'
url: https://arxiv.org/abs/2610.37517
pdf_url: https://arxiv.org/pdf/2610.37517
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: LLM推理时行为控制 · 多属性激活Steering
tags:
- activation_steering
- LLM_alignment
- multi_attribute_control
- orthogonalization
- parameterized_steering
one_liner: 提出可解释低干扰的LLM多属性激活控制方案，解决单属性校准难、多属性互相干扰问题
practical_value: '- 电商客服Agent、商品文案生成场景可直接复用多属性正交steering方案，独立控制「热情度」「专业性」「合规性」等属性，避免调热情度时意外触发过度迎合用户、夸大产品效果的问题，无需反复迭代prompt

  - 单属性steering校准技巧可直接落地：每个steering向量先识别线性单调的可操纵区间，映射到[-1,1]范围，比固定alpha值的传统steering效果稳定30%以上，避免过steering或无效果的问题

  - 参数化steering替代加法式steering，自适应调整不同输入的激活偏移量，和现有LLM推理框架适配成本低，延迟增加<10%，适合Agent实时行为控制场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有推理时activation steering技术能以极低的成本修改LLM行为，远优于prompt工程和微调，但存在两个落地核心痛点：一是单属性steering无统一校准标准，相同alpha值对不同属性的控制效果差异极大，可解释性差；二是多属性同时控制时向量互相耦合干扰，例如调整Agent的热情度会意外提高迎合用户的sycophancy程度，无法独立控制多个行为属性，限制了工业场景落地。
### 方法关键点
1. 单属性校准：为每个steering向量独立搜索线性单调的可操纵区间，将其映射到[-1,1]的统一范围，解决不同属性控制强度不统一的问题
2. 参数化steering：替代传统加法式alpha迭代steering，直接将输入激活投影到目标属性强度对应的位置，不同输入的调整量自适应，操作具备幂等性，可解释性更强
3. 多属性正交化：对多个steering向量做基变换正交化，转换为独立坐标轴，每个坐标对应一个属性，调整时互不干扰，彻底消除多属性耦合问题
### 关键实验结果
在Llama 2 7B、Qwen 3 8B上验证，对比传统alpha迭代steering：对于相关性>0.75的高耦合属性对，正交参数化方法将多属性干扰敏感度降低45%（从1.5降至0.827），属性可控范围提升107%（从1.55升至3.22）；在BBQ、Toxigen、TruthfulQA等bias控制任务上，效果与复杂的MAT-Steer方法相当，实现成本仅为其1/3。
### 最值得记住的结论
多属性steering的核心瓶颈不是向量本身的精度，而是向量空间的几何耦合，简单的线性正交化+校准就能大幅提升可控性，性价比远高于复杂的gating、非线性方法。
