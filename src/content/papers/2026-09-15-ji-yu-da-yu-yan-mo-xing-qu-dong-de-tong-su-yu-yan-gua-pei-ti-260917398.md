---
title: Enhancing Accessibility of Medical Texts through Large Language Model-Driven
  Plain Language Adaptation
title_zh: 基于大语言模型驱动的通俗语言适配提升医疗文本可及性
authors:
- Ting-Wei Chang
- Hen-Hsen Huang
- Hsin-Hsi Chen
affiliations:
- Department of Computer Science and Information Engineering, National Taiwan University,
  Taiwan
- Institute of Information Science, Academia Sinica, Taiwan
- AI Research Center (AINTU), National Taiwan University, Taiwan
arxiv_id: '2609.17398'
url: https://arxiv.org/abs/2609.17398
pdf_url: https://arxiv.org/pdf/2609.17398
published: '2026-09-15'
collected: '2026-09-17'
category: LLM
direction: 大模型文本简化 · MoA多Agent融合
tags:
- LLM
- Mixture-of-Agents
- QLoRA
- Prompt Engineering
- Text Simplification
one_liner: 结合Mixture-of-Agents与多类LLM实现医疗文本通俗适配，对比Prompt策略与QLoRA微调效果
practical_value: '- 做专业领域内容通俗化适配（如电商规格参数、药品说明、保险条款科普）时，可复用「Prompt策略对比+QLoRA微调小参数LLM」的技术路径，兼顾成本与效果

  - 多模型输出融合场景可引入MoA架构，协同优化不同LLM的输出，提升专业内容改写鲁棒性，降低关键信息丢失概率

  - 低资源领域文本改写任务可优先验证zero/few-shot Prompt效果，再按需叠加QLoRA微调，快速完成最小可行方案验证'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
专业医疗文本术语晦涩，普通患者阅读理解门槛高，现有自动化通俗语言适配（PLA）方案在少样本/零样本场景下效果有限，难以兼顾内容简化度与核心信息保留率。

### 方法关键点
1. 对比GPT-4o-mini、Gemini-1.5-pro、LLaMA等多类主流LLM在医疗PLA任务中的表现；
2. 验证不同Prompt工程策略、QLoRA微调对LLM改写效果的提升作用；
3. 引入MoA架构融合多LLM输出，提升适配任务的适应性与鲁棒性。

### 关键结果
LLM驱动的PLA方案可有效降低医疗文本阅读难度，同时完整保留核心医疗信息；MoA架构相比单模型方案鲁棒性显著提升，QLoRA微调后的小参数LLM可接近通用大模型的改写效果。
