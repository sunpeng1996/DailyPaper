---
title: 'Program-as-Weights: A Programming Paradigm for Fuzzy Functions'
title_zh: Program-as-Weights（PAW）：面向模糊函数的新型编程范式
authors:
- Wentao Zhang
- Liliana Hotsko
- Woojeong Kim
- Pengyu Nie
- Stuart Shieber
- Yuntian Deng
affiliations:
- University of Waterloo
- Cornell University
- Harvard University
arxiv_id: '2607.02512'
url: https://arxiv.org/abs/2607.02512
pdf_url: https://arxiv.org/pdf/2607.02512
published: '2026-07-01'
collected: '2026-07-03'
category: LLM
direction: LLM 轻量化部署 · 模糊函数编译
tags:
- LoRA
- PEFT
- edge-deployment
- text-to-LoRA
- fuzzy-function
one_liner: 将自然语言描述的模糊函数编译为轻量化LoRA适配器，性能追平32倍参数大模型的prompt效果
practical_value: '- 电商/推荐场景高频小任务（如评论情感分类、搜索query意图识别、垃圾内容过滤）可采用PAW范式编译为20M左右的单任务LoRA，本地部署无需调用大模型API，大幅降低推理成本、消除隐私风险、提升响应速度

  - 推理侧优化可复用「一次编译、多次执行」思路：仅在任务定义时调用一次大模型生成适配小模型的LoRA，后续请求全部由端侧/边缘侧小模型执行，适合推荐系统端侧实时个性化、Agent本地工具调用等场景

  - 可直接复用「离散伪程序+连续LoRA适配器」的混合结构：伪程序负责对模糊输入降噪对齐，LoRA负责任务专属适配，效果优于纯LoRA或纯prompt方案，可直接套用到业务多任务小模型适配场景'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大量无法用明确规则实现的模糊任务（如日志告警、异常JSON修复、搜索意图排序）均依赖调用大模型API实现，存在成本高、服务不稳定、无法离线执行、数据隐私风险等问题，亟需低成本、可本地部署的模糊任务实现方案。
### 方法关键点
- 整体采用「编译器-解释器」架构：4B参数伪编译器将用户自然语言需求转换为标准化伪程序+输入输出样例；4B参数LoRA编译器基于需求与伪程序输出专属LoRA适配器；冻结的0.6B轻量解释器加载LoRA即可执行任务
- 输出PAW程序为混合结构：离散伪程序负责模糊输入降噪，连续LoRA负责任务专属微调，单任务LoRA仅23M，支持版本管理、离线分发
- 开源10M样本规模的FuzzyBench数据集，覆盖800+类常见模糊文本任务，用于训练LoRA编译器
### 关键实验结果
在FuzzyBench验证集上，0.6B Qwen3解释器执行PAW程序的Exact Match达73.78%，超过Qwen3-32B直接prompt的68.70%，推理内存仅为后者的1/50；量化后可在MacBook M3上达到30 token/s的推理速度；输入存在拼写、语法等噪声时性能仅下降3.7%，鲁棒性优异。

大模型的角色可从每次请求都需调用的问题解决者，转变为仅调用一次的工具构建者，「大模型编译、小模型执行」是边缘AI落地的重要可行方向。
