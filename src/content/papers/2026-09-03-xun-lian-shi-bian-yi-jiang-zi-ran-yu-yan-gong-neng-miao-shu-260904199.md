---
title: 'Compile by Training: Turning Natural-Language Specifications into Local Neural
  Functions'
title_zh: 训练式编译：将自然语言功能描述转换为本地可运行神经函数
authors:
- Yuntian Deng
- Pengyu Nie
- Stuart Shieber
affiliations:
- University of Waterloo
- Harvard University
arxiv_id: '2609.04199'
url: https://arxiv.org/abs/2609.04199
pdf_url: https://arxiv.org/pdf/2609.04199
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM轻量化落地 · 训练式编译
tags:
- LoRA
- Knowledge Distillation
- Synthetic Data
- Parameter Efficient Fine-tuning
- LLM Deployment
one_liner: 通过大模型生成样本微调LoRA，将自然语言定义的功能编译为无远程依赖的本地轻量神经函数
practical_value: '- 高频窄域任务可复用该流程：用大模型生成标注样本微调小模型LoRA，替换高频远程LLM调用，降本减延迟，比如电商评论标签提取、客服固定意图分类等场景

  - 多组件Agent系统可将编译好的神经函数作为模糊决策节点，与常规代码、检索模块组合，比如电商导购Agent的意图路由、答案合并环节，兼顾灵活性和运行效率

  - 语义类任务评测可复用LEM判断逻辑：忽略格式差异仅校验核心语义，适合推荐文案生成、query改写等多合理输出场景的自动评测

  - 工程上可复用样本生成与训练并行的策略，减少微调等待时间，适配业务快速迭代小模型的需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大量高频窄域文本处理任务（如信息提取、分类）规则编码繁琐，每次调用远程大模型会产生重复成本、网络延迟，还依赖外部服务商；现有快速编译方案准确率低，无法覆盖复杂模糊任务，亟需兼顾准确率和本地运行能力的落地方案。

### 方法关键点
- 两阶段编译流程：先由教师大模型根据自然语言功能描述生成标注样本对，再用样本微调轻量LoRA适配器，适配共享的冻结果Qwen3-0.6B解释器，最终打包为可版本化、可组合的神经函数，运行时无需调用教师模型
- 工程优化：样本生成和训练并行执行，缩短编译耗时；支持教师样本缓存、多GPU任务调度，适配交互式使用场景；编译产物可像普通软件一样存储、版本管理、与常规代码组合调用
- 评测设计：提出LEM（LLM Exact Match）指标，由大模型判断输出语义正确性，忽略空格、JSON格式等非核心差异，更贴合模糊任务的评测需求

### 关键实验
在FuzzyBench-Hard数据集（PAW快速编译器完全无法精确匹配的任务子集）上，对比PAW快速编译器，训练式编译的语义准确率从22.4%提升至83.6%，编译耗时约50.9秒（快速编译器仅3.5秒）；混合2:1的GPT-5.4-mini和GPT-5.5生成样本，比单用mini教师准确率提升10.5个百分点，2400条独有样本即可达到83.6%的准确率。

大模型可作为构建工具的上游能力，而非业务运行时的必须依赖，通过编译为本地神经函数可兼顾模糊任务灵活性和落地的成本、延迟要求。
