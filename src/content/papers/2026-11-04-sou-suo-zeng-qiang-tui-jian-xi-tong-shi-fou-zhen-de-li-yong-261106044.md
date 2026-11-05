---
title: Do Search-Augmented Recommenders Use the Latest Search Episode?
title_zh: 搜索增强推荐系统是否真的利用了最新搜索会话？
authors:
- Jiandong Ding
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.06044'
url: https://arxiv.org/abs/2611.06044
pdf_url: https://arxiv.org/pdf/2611.06044
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 搜索增强推荐 · 反事实归因诊断
tags:
- Search-augmented Recommendation
- Counterfactual Evaluation
- Attribution
- Recommendation Diagnosis
- SAR
one_liner: 提出FocalSwap反事实测试协议，发现搜索增强推荐的搜索贡献归因高度依赖控制组选择，最新会话正向贡献未证实
practical_value: '- 做搜索增强推荐（SAR）的特征归因时，不能仅依赖中性mask ablation，需补充真实匹配搜索序列的替换对照，避免把OOD导致的效果下降错判为搜索特征的真实贡献

  - 可直接复用FocalSwap固定行对照框架，排查业务SAR模型中最新搜索会话、历史搜索序列的真实贡献，减少无效特征迭代

  - 开源UniSAR、SESRec等主流SAR模型对最新搜索会话的利用程度极低，业务落地时不要过度预期实时搜索会话的收益，建议优先做长周期搜索兴趣建模'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索增强推荐（SAR）的效果验证多依赖整体模块ablation，无法区分收益来自训练阶段的搜索表征积累、历史搜索状态还是最新实时搜索会话；且常用的中性mask ablation可能引入OOD偏差，导致归因结果严重偏离实际。

### 方法关键点
- 提出FocalSwap固定行反事实测试框架：固定每个样本的用户预搜索历史、推荐目标、候选集、模型权重，仅替换最新搜索会话/全部搜索序列，对比不同控制组下的RR变化
- 两类控制组设计：中性ID mask组、真实数据中类别/用户画像匹配的搜索序列替换组；同时引入planted signal、GenSAR原生查询任务验证协议的检测有效性
- 三个核心观测指标：目标排名变化率、RR差值的正负贡献、真实搜索vs替换搜索的半平局计分胜率

### 关键实验
在KuaiSAR、Qilin公开SAR数据集上测试开源SESRec、3个独立训练的UniSAR checkpoint，覆盖66139条公共样本：
1. 全部搜索序列用中性mask替换时，RR提升2.77×10⁻³~6.604×10⁻³，59.7%~61.7%的目标排名发生变化，初步显示存在搜索贡献
2. 用匹配的真实搜索序列替换时，无统计显著的正向贡献，仅44.1%~44.8%的排名发生变化
3. 仅替换最新搜索会话时，所有模型的正向贡献均未通过统计检验，无证据显示模型实际利用了最新搜索会话

### 核心结论
搜索增强推荐的特征归因结论高度依赖控制组选择，仅靠中性mask ablation得到的搜索特征贡献存在严重高估风险。
