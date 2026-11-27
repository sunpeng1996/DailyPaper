---
title: 'Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles
  with Community-Verified Answers'
title_zh: Puzzling-Bench：基于23777道社区验证谜题的大语言模型评测基准
authors:
- Abhinav Sharma
- Li Li
- Chien Van Nguyen
- Sai Karthik Navuluru
- Bo Ni
- Xiangbo Gao
- Xiaolei Huang
- Yue Zhao
- Nesreen K. Ahmed
- Tyler Derr
affiliations:
- University of Massachusetts Amherst
- University of Southern California
- University of Oregon
- University of Texas at Dallas
- Vanderbilt University
arxiv_id: '2611.34331'
url: https://arxiv.org/abs/2611.34331
pdf_url: https://arxiv.org/pdf/2611.34331
published: '2026-11-24'
collected: '2026-11-27'
category: Eval
direction: 大语言模型推理能力评测基准建设
tags:
- Benchmark
- LLM Evaluation
- Reasoning
- Multimodal
- Data Contamination
one_liner: 构建含23777道社区验证多模态谜题的LLM评测基准，验证两层评分方案并完成9款主流模型评测
practical_value: '- 两层评分方案（先标准化精确匹配再LLM评审）可直接复用在生成式推荐文案、Agent交互输出的自动评测流程，降低人工标注成本

  - 训练截断后切片做数据污染检测的设计思路，可迁移到LLM4Rec微调数据集清洗、模型效果验证环节

  - 多模态输入缺失对性能影响的量化评估方法，可用于电商图文推荐的模态重要性分析与输入容错设计'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM推理能力评测基准普遍存在数据污染、题型覆盖窄、答案验证不足等缺陷，缺少同时覆盖逻辑推理、发散思维、多模态输入的标准化评测数据集。
### 方法关键点
1. 基于Puzzling Stack Exchange 2014-2026年数据构建23777道带社区验证答案的谜题数据集，覆盖谜语、密码、逻辑题、休闲数学等类型，1/3样本带图片，配套作者提示、分类标签、创建时间，支持提示消融、类别分析、训练截断后切片的数据污染检测；
2. 采用两层评分机制：先做标准化精确匹配，再用LLM评审，跨模型家族的评审一致性达95%-97%，kappa 0.82-0.96，无自身模型家族偏好。
### 关键结果
GPT-6.1在255题共享测试集上准确率达74.8%，17道难题击败全部9款测试模型，多模态测试中移除图片会让Top2模型性能下降24、35个百分点，9模型的oracle集成准确率达91%
