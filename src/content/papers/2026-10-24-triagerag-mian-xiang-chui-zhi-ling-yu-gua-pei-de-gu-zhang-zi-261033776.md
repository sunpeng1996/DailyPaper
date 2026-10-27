---
title: 'TriageRAG: Failure-Aware Self-Training for Adapting Retrieval-Augmented Language
  Models to Specialized Domains'
title_zh: TriageRAG：面向垂直领域适配的故障感知自训练RAG方法
authors:
- Samarth Varshney
- Ritu Yadav
arxiv_id: '2610.33776'
url: https://arxiv.org/abs/2610.33776
pdf_url: https://arxiv.org/pdf/2610.33776
published: '2026-10-24'
collected: '2026-10-27'
category: RAG
direction: RAG 垂直领域无标注自训练优化
tags:
- RAG
- Self-training
- Domain Adaptation
- LoRA
- QA
one_liner: 通过故障分类路由自生成样本，无标注下提升垂直领域RAG问答性能
practical_value: '- 做电商/广告垂直领域RAG（如商品问答、客服机器人、规则咨询）时，不要仅用round-trip过滤的样本训练，可加入10-20%检索失败样本做参数SFT，让模型学会不盲信检索结果，避免检索噪声拉低整体效果

  - 自训练RAG时可通过低成本开闭卷探针将样本划分为四类，按优先级路由训练：优先训练上下文失败的硬样本，检索失败样本用于校准模型对检索结果的信任度，减少无效训练

  - 不要直接用检索失败的query-正例对微调检索器，论文实测会引入噪声降低整体召回，除非配套更干净的正负例构造逻辑

  - 样本分类的分布可直接作为无标注诊断工具，快速定位RAG瓶颈是模型知识不足、上下文理解能力差还是检索召回低，无需标注测试集'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
通用RAG适配医疗、电商等垂直领域时，标注QA数据稀缺成本高，现有自训练方案（如SimRAG）对所有过滤后的样本统一训练，既不区分模型是否已掌握对应知识，也不定位错误来自检索模块还是阅读模块；且round-trip过滤规则会移除所有检索失败的样本，导致模型从未见过无效上下文，过度信任检索结果，在检索召回低的场景效果反而不如闭卷模型。
### 方法关键点
- 阶段1：用通用检索导向QA数据对底座模型做LoRA微调，使其具备问答、答案抽取、答案引导式问题生成能力
- 阶段2每轮迭代流程：
  1. 从无标注领域语料生成(q,a,d)三元组，仅保留模型看原文可答对的自可答样本
  2. 用开闭卷探针测试模型：计算闭卷准确率p_cb、开卷准确率p_ob、证据是否在检索结果中h，按阈值将样本分为4类：KNOWN（模型已掌握）、SOLVED（开卷可答对）、CONTEXT-FAILURE（证据在上下文但答不对）、RETRIEVAL-FAILURE（证据未检索到）
  3. 按60%/20%/15%/5%配额采样四类样本：上下文失败样本做普通RAG SFT，检索失败样本做参数SFT（要求模型在无证据的上下文中输出正确答案，校准对检索结果的信任度），其余做巩固训练
  4. LoRA微调后更新模型，进入下一轮
### 关键结果
在医疗、自然科学、计算机科学3个领域11个数据集测试，底座用Qwen3-4B/8B，对比同预算的SimRAG、RAFT等基线，TriageRAG效果高出1.2~6.4个点，是唯一能在检索拖累基线的场景下恢复到闭卷水平的方法，8B模型下比随机采样高2.3个点。
> 最值得记住的结论：Round-trip过滤会移除所有无证据的训练上下文，从未见过无效上下文的读者会过度信任有噪声的检索结果。
