---
title: 'PACE: A Proxy for Agentic Capability Evaluation'
title_zh: PACE：低成本代理型Agent能力评估框架
authors:
- Yueqi Song
- Lintang Sutawika
- Jiarui Liu
- Lindia Tjuatja
- Jiayi Geng
- Yunze Xiao
- Daniel Lee
- Aditya Bharat Soni
- Vincent Lo
- Xiang Yue
affiliations:
- Carnegie Mellon University
- Salesforce AI Research
arxiv_id: '2607.02032'
url: https://arxiv.org/abs/2607.02032
pdf_url: https://arxiv.org/pdf/2607.02032
published: '2026-07-01'
collected: '2026-07-03'
category: Eval
direction: Agent能力评估 · 低成本代理基准
tags:
- Agent Evaluation
- Benchmark Compression
- Proxy Evaluation
- LLM Agent
- Low-cost Eval
one_liner: 用低成本非Agent基准子集预测Agent基准性能，成本降至原1%以内
practical_value: '- 业务Agent选型（如电商导购Agent、广告投放Agent）时，可复用PACE思路，先跑低成本单能力benchmark（工具调用、指令遵循、推理）筛选Top候选，再做全链路Agent评估，可降低90%以上的评估成本与周期

  - 推荐/广告系统LLM模块迭代时，可借鉴「局部相关性+全局信息量」的实例选择策略，快速构建与线上效果强相关的低成本离线评估集，加速超参数、Prompt、LoRA微调版本的迭代效率

  - 做Agent效果评估时，可复用bootstrap重采样降噪的trick，降低小样本评估的结果波动，提升离线指标与线上业务效果的相关性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent类基准（如GAIA、SWE-Bench）评估需要搭建复杂运行环境、多次交互调用，单模型评估成本可达数千美元、耗时数天，严重拖慢Agent模型迭代、选型效率；而指令遵循、推理、工具调用等非Agent单能力基准成本极低（单实例成本仅为Agent基准的1/100甚至更低），但此前缺乏可靠的关联方法，无法用低成本基准代理高成本Agent评估。

### 方法关键点
- 将任务定义为预算约束下的非Agent实例子集选择问题，同时支持Agent基准绝对得分预测、模型间相对排名预测两个核心场景
- 实例选择融合双互补策略：局部策略按实例得分与Agent基准得分的Spearman相关性排序选高相关实例；全局策略结合SVD杠杆得分（衡量实例全局信息密度）与相关性，选信息密度高且和目标相关的实例，两者合并为100个实例的最终子集
- 预测层采用bootstrap重采样降噪的线性回归，降低Agent基准小样本标签的噪声影响，提升预测稳定性

### 关键结果
在4个主流Agent基准、19个覆盖11类核心能力的非Agent基准、14款主流开源/闭源LLM上验证，留一交叉验证下平均MAE为3.8%，Spearman相关性达0.81，模型两两排名准确率约85%；同等预测质量下，评估成本仅为随机采样Agent基准实例的1/100，不到全量Agent评估成本的1%。

只要筛选策略得当，低成本的单能力静态基准完全可以精准预测Agent复杂任务的性能，大幅降低Agent研发的评估门槛。
