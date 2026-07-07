---
title: 'Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation
  Against Fine-Tuning Poisoning'
title_zh: 仅学习有效适配器可表达内容：对抗微调投毒的子空间约束适配方法
authors:
- Fabien Polly
affiliations:
- Independent Researcher
arxiv_id: '2607.05300'
url: https://arxiv.org/abs/2607.05300
pdf_url: https://arxiv.org/pdf/2607.05300
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: LLM参数高效微调 · 投毒防御
tags:
- LoRA
- Parameter Efficient Fine-Tuning
- Poisoning Defense
- Subspace Learning
- OOD Detection
one_liner: 基于可信LoRA适配器池的子空间约束微调方法，在保留干净数据性能的同时大幅提升投毒抵抗能力
practical_value: '- 电商/广告场景用公开LoRA做业务适配时，可复用该子空间约束方案，避免用户上传的投毒训练数据（比如恶意评论、虚假标注）污染情感分类、商品标签生成等业务模型

  - 适配流程可直接复用论文的损失差阈值做OOD检测，垃圾/投毒数据的适配损失是干净数据的120倍，不需要额外开发检测逻辑即可自动拦截异常训练数据

  - 多任务持续微调场景下，在可信LoRA池的子空间内适配可降低灾难性遗忘，遗忘波动比普通LoRA小4倍左右，适合电商多品类、多业务线的Adapter复用场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
PEFT（如LoRA）虽然参数效率高，但可表达的权重更新空间仍然过大，仅需数百条投毒数据就能破坏对齐后的模型，现有防御多为正则约束或数据过滤，没有从根本上限制有害更新的可表达性，存在被攻击者绕过的风险。

### 方法关键点
- 收集可信的公开LoRA适配器池，计算所有适配器delta W的Gram矩阵，做特征分解取top K主成分作为共享子空间的正交基
- 微调时仅优化子空间内的K维坐标z，基模型和适配器池完全冻结，最终的权重更新是池中适配器的线性组合，可表达范围严格限制在池的仿射子空间内
- 适配损失天然作为OOD信号，损失过高直接判定数据不在池覆盖范围内，可自动拦截

### 关键实验结果
基于Flan-T5-large（783M）+ 196个LoraHub公开适配器实验，对比普通rank16 LoRA：
1. 干净数据下K=128的子空间约束适配性能和普通LoRA完全持平
2. 100%标签反转投毒下，普通LoRA的精确匹配率跌到3%-26%，约束方法保持62%-96%
3. 垃圾数据的适配损失是干净数据的120倍，AUROC=1.0可完全区分
4. 自适应后门攻击下，目标行为不在池覆盖范围内时攻击成功率仅8%，远低于LoRA的100%

### 核心结论
子空间约束的防御能力完全取决于可信适配器池的覆盖范围，仅能阻止池本身不能表达的有害行为。
