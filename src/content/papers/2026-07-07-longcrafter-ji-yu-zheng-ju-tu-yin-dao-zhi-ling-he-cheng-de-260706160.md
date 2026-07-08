---
title: 'LongCrafter: Towards Diverse Long-Context Understanding via Evidence-Graph-Guided
  Instruction Synthesis'
title_zh: LongCrafter：基于证据图引导指令合成的长上下文理解框架
authors:
- Chenhao Yuan
- Yinhao Xu
- Shuwen Xu
- Xizhi Yang
- Jiaxiang Liu
- Chenxi Zhou
- Shaoping Huang
- Haolin Ren
- Pengfei Cao
- Jun Zhao
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.06160'
url: https://arxiv.org/abs/2607.06160
pdf_url: https://arxiv.org/pdf/2607.06160
published: '2026-07-07'
collected: '2026-07-08'
category: LLM
direction: 长上下文LLM · SFT数据合成
tags:
- Long-Context
- SFT
- Evidence Graph
- Instruction Synthesis
- Faithful Reasoning
one_liner: 提出层级任务分类+证据图引导的长上下文SFT数据合成框架 显著提升LLM长上下文理解性能
practical_value: '- 搭建电商/广告场景的长上下文RAG Agent时，可复用证据图引导的指令生成方法，构造跨多商品详情、用户评价、平台规则的多跳问答训练数据，大幅提升Agent推理忠实度，减少幻觉

  - 训练长上下文召回/排序模型时，可复用其32种细粒度任务分类体系，构造覆盖从局部属性匹配到全局多跳依赖推理的分层训练任务，提升模型对分散证据的利用能力

  - 可借鉴其证据锚定的响应生成范式，要求LLM生成推荐理由、营销文案时必须引用原始商品/用户行为证据，降低生成内容的事实错误

  - 针对长上下文「lost in the middle」问题，可复用其平衡难度分布的训练数据构造方法，仅需少量高质量结构化数据即可显著提升模型对中间位置证据的定位能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文SFT数据合成方法普遍存在三大缺陷：任务覆盖范围窄、指令难度不足、缺乏忠实度监督，导致模型易学习位置或表面特征捷径，无法处理复杂跨段落推理，还易引入参数知识产生幻觉，且普遍存在「lost in the middle」问题，难以支撑电商咨询、个性化推荐、Agent决策等场景下的长文档理解、多跳推理需求。
### 方法关键点
- 设计覆盖本地/浅层到全局/深层的2层级、32细粒度任务的层级分类体系，作为数据合成的全局先验，覆盖检索、排序、状态追踪、多证据推理等12类核心能力
- 三阶段结构化数据合成流程：1）长上下文构造：单文档匹配对应任务，多文档采用BM25+稠密检索混合召回相关文档，保证上下文主题相关且无冗余；2）证据约束图构造：先抽取所有候选证据跨度，再针对目标任务构建最小证据图，节点为带位置标记的证据片段，边为跨段落依赖（时序、因果、共指等）；3）指令-响应对合成：指令要求必须联合所有证据节点才能作答，避免单段可答的捷径问题，响应采用逐步骤引用原文证据的格式，杜绝外部参数知识引入
- 合成后通过LLM校验指令的明确性、可答性、答案唯一性，过滤不合格样本
### 关键实验
仅用2000条合成数据做LoRA SFT，在Qwen2.5-7B、LLaMA-3.1-8B两个开源骨干上，在LongBench、LongBench v2、LooGLE三个权威长上下文基准的All-Overall得分分别达45.15%、45.71%，比对应官方后训练模型分别高2.41、5.25个点，比次优SFT基线分别高5.8、5.3个点；训练后的模型证据定位不受位置影响，几乎完全解决「lost in the middle」问题。
### 最值得记住的一句话
少量结构化、难度分层、证据锚定的高质量SFT数据，效果远超过大量无结构、低难度的长上下文训练数据。
