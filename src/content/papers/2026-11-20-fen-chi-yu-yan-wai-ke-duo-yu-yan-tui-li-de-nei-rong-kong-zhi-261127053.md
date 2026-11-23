---
title: 'Isolating the Language Shell: A Content-Controlled Study of Multilingual Reasoning'
title_zh: 分离语言外壳：多语言推理的内容控制研究
authors:
- Hoejoon Kwon
- Jinhee Jang
- Byeonggeuk Lim
- YoungBin Kim
affiliations:
- Chung-Ang University
- NEXON
- KETI
arxiv_id: '2611.27053'
url: https://arxiv.org/abs/2611.27053
pdf_url: https://arxiv.org/pdf/2611.27053
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 多语言LLM推理 监督语言选择优化
tags:
- Multilingual Reasoning
- Chain-of-Thought
- Supervised Fine-tuning
- Knowledge Distillation
- LLM Training
one_liner: 通过内容控制实验验证多语言推理蒸馏中监督语言外壳的独立影响
practical_value: '- 多语言电商客服/导购Agent做推理SFT时，不要仅凭预训练perplexity过滤低兼容性的混合语言监督语料，其在复杂任务上的准确率可能比高兼容性的纯目标语监督高10pp以上

  - 若业务要求多语言应用的输出必须符合当地语言规范，优先选择翻译后的目标语推理链做监督，可在准确率损失极小的前提下，将输出的目标语占比从不足1%提升至70%以上

  - 跨境电商搜索推荐场景下的多语言query理解SFT，可尝试混合语言监督（英语推理框架+本地语言实体/术语），平衡推理准确率和本地语义理解效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言推理蒸馏研究的监督语料通常混杂了语言形式、推理内容、生成翻译过滤流程等多种变量，无法明确语言外壳本身对下游模型效果的独立影响，同时行业普遍使用的预训练兼容性指标是否能指导监督语言选择也缺乏严谨验证。

### 方法关键点
- 构建内容严格对齐的三版本监督数据集：将同一条经过验证的英语CoT推理轨迹，分别渲染为原生英语、目标语言全翻译、英-目标语混合（英语推理框架+本地实体）三种语言外壳，推理步骤、公式、中间结论、最终答案完全一致
- 选取Qwen3-4B、Gemma3-4B两个通用预训练底座，分别在韩语、中文、德语三种语言的控制数据集上执行全参数SFT，所有训练配置完全对齐
- 从三个维度系统评估效果：预训练兼容性（监督语料的token级perplexity）、下游学习能力（多语言数学推理准确率）、外壳继承性（生成结果的目标语言占比）

### 关键实验结果
- 训练集来自对齐后的GSM8K共7.2K条样本，评测使用PolyMath的低、中两个难度子集
- 预训练兼容性排序稳定（英语>翻译>混合）但完全无法预测下游准确率：Qwen在韩语中等难度任务上，兼容性最低的混合外壳比翻译外壳准确率高15.2pp
- 5个统计显著的效果差异均出现在Qwen上，均为英语/混合外壳优于翻译外壳，Gemma无显著差异
- 准确率相近的前提下，英语外壳训练的模型输出目标语言占比<1%，翻译外壳的占比>70%，输出语言行为差异极大

### 核心结论
多语言推理蒸馏的监督语言外壳选择是场景依赖的多目标决策，不能仅靠预训练兼容性或单一准确率指标判断
