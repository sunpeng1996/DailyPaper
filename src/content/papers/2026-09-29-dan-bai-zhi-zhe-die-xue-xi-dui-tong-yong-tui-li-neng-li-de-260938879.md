---
title: Does Learning Protein Folding Generalize to Broader Reasoning?
title_zh: 蛋白质折叠学习对通用推理能力的泛化性研究
authors:
- Yong Liu
- Zhanpeng Shi
- Yizhou Dang
- Zhongyue Zhang
- Xiaoliang Shi
- Zhijian Wei
- Shuangjia Zheng
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- Shanghai Innovation Institute
- Northeastern University
arxiv_id: '2609.38879'
url: https://arxiv.org/abs/2609.38879
pdf_url: https://arxiv.org/pdf/2609.38879
published: '2026-09-29'
collected: '2026-10-05'
category: LLM
direction: LLM推理能力提升 · 跨领域监督信号
tags:
- LLM
- Reasoning
- Cross-domain Training
- LoRA
- Protein Folding
one_liner: 通过蛋白质折叠结构数据后训练LLM，跨10类推理基准平均提升准确率3.23个百分点
practical_value: '- 跨领域结构化监督信号可低成本提升LLM推理能力，电商/推荐场景可复用商品属性、用户行为的结构化数据作为额外后训练信号，提升推荐Agent的逻辑推理、多约束匹配能力

  - 训练阶段引入任务专用头、推理阶段仅保留LoRA权重的架构，不会增加推理开销，适合搜索推荐、广告等对latency要求高的实时业务场景

  - 结构化微调数据存在边际效应递减，业务侧可先做小批量规模实验找到最优数据量，无需盲目堆数据节省算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM训练高度依赖人类文本数据，这类数据往往仅包含表层答案，缺乏背后的空间、结构逻辑，且人类文本数据即将触达规模天花板，亟需探索新的跨领域监督信号提升LLM通用推理能力；蛋白质折叠任务有大量可自动校验的结构数据，是理想的测试场景。

### 方法关键点
- 构建FoldingCorpus数据集：从公开蛋白质结构库中生成14400条结构相关问答对，覆盖12类结构推理任务，所有答案可通过坐标自动校验
- 提出Fold2Reason后训练范式：冻结LLM主干，仅微调LoRA权重，同时引入两个互补监督信号：通过原生语言头预测离散结构问答答案、通过冻结的几何解码器从共享表征中解码连续3D结构，梯度仅回传至LoRA和共享工作空间
- 推理阶段仅保留微调后的LoRA权重，移除所有蛋白质相关模块，无额外推理开销

### 关键结果
基于Qwen3.5-9B的模型在10类覆盖空间、图、科学、通用推理的基准上，将宏观平均准确率从45.09%提升至48.33%，+3.23pp，所有10个基准均获得正向收益；蛋白质折叠任务得分是基线Qwen3.5-9B的2.7~3.5倍；数据规模实验显示2000个蛋白质时推理提升达到峰值3.70pp，之后出现边际递减。

最值得记住的一句话：非语言的、结构密集的科学领域数据，可以系统性提升语言模型的通用推理能力，已解决的科学问题可作为LLM后训练的实用监督来源。
