---
title: 'JEPA-Anything: Learning Predictive Models across Different Worlds'
title_zh: 《JEPA-Anything：跨异质领域学习通用预测模型》
authors:
- Taoyong Cui
- Zhongyao Wang
- Xinyue Xu
- Weiyang Liu
- Zhaochen Yu
- Yuying Zhang
- Qiang Gao
- Mengyue Yang
- Wanli Ouyang
- Pheng Ann Heng
affiliations:
- PHAI Labs
arxiv_id: '2609.20800'
url: https://arxiv.org/abs/2609.20800
pdf_url: https://arxiv.org/pdf/2609.20800
published: '2026-09-16'
collected: '2026-09-18'
category: Other
direction: 跨领域世界建模 · 正交预测因子分解
tags:
- JEPA
- World Modeling
- Predictive Factorization
- Cross-domain Learning
- Representation Learning
one_liner: 提出基于正交预测因子分解的跨领域通用世界建模框架，7类任务性能全面优于JEPA基线
practical_value: '- 跨业务域（搜索/推荐/广告）统一建模可借鉴正交预测因子分解思路：将共同预测目标拆分为互补因子，共享底层预测架构，降低重复建模成本

  - 用户行为序列、商品销量等长时序预测场景可复用「因子拆分+专用通路学习+共享重组」架构，提升OOD泛化与长周期预测精度

  - 交互类Agent的世界建模模块可参考该通用设计，降低不同业务场景下的模型适配成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有世界预测模型均为领域定制，缺乏跨异质系统通用的学习范式，无法支撑多场景下的统一预测与干预决策。
### 方法关键点
基于正交预测因子分解（OPF）构建领域无关框架JEPA-Anything，扩展联合嵌入预测架构，将隐层目标拆分为互补因子，通过专用通路学习后在共享预测结构中重组。
### 关键结果
- 在7个领域（视觉、生物、临床轨迹等）完成验证，10个动力学任务指标全面优于匹配JEPA基线，Interventional Pong单干预预测误差降低34.8%
- 4类系统的分子动力学预测中，1步与100步预测误差均为所有对比方法最低
- 生成的生物干预方案在细胞、类器官、小鼠等多轮实验中获得验证
