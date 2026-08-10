---
title: 'SABRE: Scalable and Automated Benchmarking of VLMs under Stress'
title_zh: SABRE：压力场景下视觉语言模型的可扩展自动化基准框架
authors:
- Zixuan Lan
- Luzhe Sun
- Matthew R. Walter
- Jiawei Zhou
affiliations:
- University of Chicago
- Toyota Technological Institute at Chicago
- Stony Brook University
arxiv_id: '2608.07435'
url: https://arxiv.org/abs/2608.07435
pdf_url: https://arxiv.org/pdf/2608.07435
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: 多模态大模型压力测试基准构建
tags:
- VLM
- Benchmark
- Stress Test
- Multimodal Eval
- Automated Pipeline
one_liner: 提出可扩展自动化VLM压力测试构建框架SABRE，解决现有基准迭代慢难暴露缺陷的问题
practical_value: '- 做电商多模态商品理解VLM性能评估时，可复用SABRE的「自动化样本生成+过滤+轻量人工校验」流水线，快速构建定向压力测试集，比如反常识商品图、属性错配图的识别测试

  - 针对多模态搜索/推荐的bad case，可基于Test Primer定义任务schema，批量生成同类反例做模型迭代的回归测试，大幅降低测试集构建成本

  - 做多模态内容风控时，可复用该框架快速生成对抗性测试样本，验证模型对虚假宣传图、P图改属性商品的识别准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
VLM迭代速度远快于配套基准开发速度，固定基准易饱和，无法快速暴露模型依赖世界先验而非实际视觉输入的缺陷，且人工构建压力测试样本成本极高。
### 方法关键点
1. 构建端到端SABRE流水线：输入带数据schema的Markdown格式Test Primer，自动生成结构化任务规则、编辑/生成对应图像、构造匹配问答对；
2. 难例筛选机制：用Filtering VLM自动过滤易解决的简单样本，仅保留挑战型候选，再通过轻量人工校验修正标注、修复局部异常图像；
3. 首次实例化SABRE-Prior测试集，覆盖场景异常、材质反事实、属性不符、语言诱导4类测试场景。
### 关键结果
6款主流VLM在SABRE-Prior上的宏观平均准确率仅17.8%~31.3%，均值22.6%；框架同时支持计数、空间关系等其他VLM压力测试场景的快速定制。
