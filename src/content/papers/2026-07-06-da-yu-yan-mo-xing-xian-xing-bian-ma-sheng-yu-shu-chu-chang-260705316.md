---
title: How Much is Left? LLMs Linearly Encode Their Remaining Output Length
title_zh: 大语言模型线性编码剩余输出长度的机制探测研究
authors:
- Mohamed Amine Merzouk
- Dmitri Carpov
- Mirko Bronzi
- Damiano Fornasiere
- Adam Oberman
affiliations:
- Mila, Quebec AI Institute
- McGill University
- LawZero
arxiv_id: '2607.05316'
url: https://arxiv.org/abs/2607.05316
pdf_url: https://arxiv.org/pdf/2607.05316
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: LLM可解释性 · 内部长度表示探测
tags:
- Linear Probing
- LLM Interpretability
- Length Encoding
- OOD Generalization
- Mechanistic Study
one_liner: 通过线性探针验证7-8B指令微调LLM隐层存在通用剩余输出长度表示，可检测推理反悔
practical_value: '- 部署LLM驱动的电商导购/客服Agent时，可在prompt侧加轻量线性探针提前预判输出长度，超过token预算直接终止重调度，降低推理成本

  - 监测剩余长度探针的异常跳升信号，可快速识别LLM推理反悔/幻觉的发生，及时触发重生成或人工接管，提升回复可靠性

  - 生成式推荐场景（如商品文案、营销话术生成）中，可基于探针输出动态校准生成长度，精准匹配不同展示坑位的字数要求

  - 业务落地可直接使用多自然语言任务训练的通用长度探针，无需单场景单独拟合，泛化性优于合成数据训练的探针'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
自回归LLM逐token生成时无显式长度控制变量，但实际输出长度却呈现极强的规律性（如数学题回答稳定在3-5行、事实检索为短句），此前无法确定这种规律是解码的统计巧合，还是模型内部确实维护了剩余输出长度的计划式表示，明确该机制对LLM推理成本控制、异常检测、生成效果优化都有重要落地价值。

### 方法关键点
- 冻结3款7-8B参数级指令微调LLM（Llama3.1-8B、Olmo3-7B、Mistral-7B-Instruct-v0.3）参数，仅训练无激活的线性探针，从残差流隐层预测剩余生成token数，确保探测到的信号为LLM本身已有的线性可及信息
- 设计多组对照：仅用prompt末尾隐层预测总长度的Completion Length Probe、逐位置读取隐层的Remaining Count Probe，对比统计中位数基线、基于prompt预测值逐位减1的精确倒计时基线
- 覆盖7类数据集：2类合成计数数据集、5类自然语言数据集（GSM8K、MATH、MMLU-Pro、OpenThoughts-1k、TriviaQA），补充跨数据集泛化测试验证信号通用性

### 关键结果
- Prompt末尾即可线性解码总输出长度，MAE仅为统计基线的20%~80%，合成计数数据集上误差低至5.27 tokens
- 逐位置剩余长度预测MAE比统计基线低10%~96%，部分场景优于精确倒计时基线，说明生成过程中模型会动态更新长度估计
- 自然语言数据集训练的探针可跨任务泛化到合成数据集，反之则无法迁移，验证存在通用的长度编码方向
- 模型输出反悔语句（如Wait、let's check）时，探针预测值会异常上升，该特征是位置类基线无法复现的

### 最值得记住的结论
LLM隐层确实存在线性可读取的剩余输出长度表示，这种表示不是统计巧合，而是具备计划属性的内部状态。
