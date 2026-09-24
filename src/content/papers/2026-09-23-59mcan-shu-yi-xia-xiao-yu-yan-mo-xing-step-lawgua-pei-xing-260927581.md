---
title: Does Step Law Transfer to Small-Scale Language Models? An Empirical Recalibration
  Below 59M Parameters
title_zh: 59M参数以下小语言模型Step Law适配性实证校准
authors:
- Egor Romanyukov
- Timofey Novikov
- Timur Shokarov
- Elizaveta Zorkina
- Anastasia Palienko
- Stepan Dergachev
affiliations:
- HSE University, Faculty of Computer Science
arxiv_id: '2609.27581'
url: https://arxiv.org/abs/2609.27581
pdf_url: https://arxiv.org/pdf/2609.27581
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 小语言模型训练 · 超参数校准
tags:
- Scaling Law
- Small LLM
- Hyperparameter Tuning
- Learning Rate
- Batch Size
one_liner: 验证59M以下小语言模型仍符合Step Law幂律形式，给出适配该区间的学习率批量最优系数
practical_value: '- 训练<59M的轻量化推荐/Agent小模型时，不要直接用原Step Law计算学习率，其会高估2.4~6.6倍，建议用论文给出的新幂律系数计算初始值，大幅减少调参成本

  - 单GPU训练小模型时，可复用最优batch size仅与训练数据量正相关、与模型参数量无关的结论，固定batch size后仅调学习率即可，降低调参复杂度

  - 做小模型预训练/微调的超参数搜索时，可借鉴对数坐标下损失面局部二次逼近的方法快速定位最优超参数，无需全网格搜索'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
原Step Law仅在59M~1B参数LLM区间完成校准，<59M的小模型区间无实证验证，该区间广泛用于单GPU训练、轻量化Agent/推荐小模型、端侧模型等场景，降本需求突出。
### 方法关键点
基于nanoGPT/TinyStories训练管线，采用AdamW优化器+warmup-cosine学习率调度，通过对数坐标下平滑训练损失面的局部二次逼近，提取不同参数规模N、训练数据量D组合下的最优学习率η*与批量大小B*，共完成935次有效实验覆盖29组(N,D)配置。
### 关键结果
小模型区间仍符合Step Law幂律形式，给出适配该区间的η*、B*计算公式，R²分别达0.834、0.950；原Step Law系统高估最优学习率，中位数误差达4倍，范围2.4~6.6倍；最优B*与模型参数量N无关的结论仍成立，但其随D的增长斜率为原结果的近2倍。
