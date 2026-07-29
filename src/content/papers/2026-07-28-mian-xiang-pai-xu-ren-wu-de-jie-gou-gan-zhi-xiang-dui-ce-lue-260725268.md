---
title: Structure-aware Relative Policy Optimization for Ranking
title_zh: 面向排序任务的结构感知相对策略优化框架SRPO
authors:
- Yiteng Tu
- Weihang Su
- Zitao Su
- Yiqun Liu
- Min Zhang
- Qingyao Ai
affiliations:
- Tsinghua University
- Renmin University of China
arxiv_id: '2607.25268'
url: https://arxiv.org/abs/2607.25268
pdf_url: https://arxiv.org/pdf/2607.25268
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 排序优化 · RL排序策略优化
tags:
- Ranking
- Reinforcement Learning
- Policy Optimization
- GRPO
- Kendall-tau Distance
one_liner: 为基于RL的排序引入结构感知优势估计，解决GRPO更新激进、信用分配不准的问题
practical_value: '- 现有基于GRPO优化的RL排序链路（电商搜索/广告排序、多目标全局优化场景）可直接替换为SRPO，无需改动采样逻辑，即可降低策略更新波动，同时提升NDCG、公平性等全局指标

  - 排序结构相似度计算可复用论文提出的top-weighted Kendall-tau距离，头部权重和NDCG等业务指标对齐，比普通Kendall-tau更适合排序任务的相似度度量

  - 冷启动query、少曝光商品等有限反馈场景可直接采用SRPO的G=8小采样组配置，相比GRPO需要G=64的配置采样成本降低87.5%，同时抗用户行为噪声能力更强

  - 多目标排序场景下采用SRPO可避免为了单一目标大幅打乱原有排序结构，保障线上流量稳定性的同时实现多目标帕累托提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RL-based排序方法（如适配排序的GRPO）将每个采样的排序列表视为原子输出，仅通过标量reward归一化计算优势，完全忽略不同排序列表的结构差异：reward接近的列表可能结构差异极大，仅调整头部顺序得到的高reward样本和全局打乱得到的高reward样本会获得同等优化信号，导致策略更新过于激进、信用分配不准确，训练稳定性差，在有限反馈、多目标优化等场景下问题尤为突出。
### 方法关键点
- 采用**top-weighted Kendall-tau距离**衡量两个排序的结构差异，给头部位置的顺序差异分配更高权重，天然贴合搜索/推荐排序的头部敏感特性
- 对同组内的排序对，用reward差值除以结构距离得到结构归一化偏好，衡量每单位排序调整带来的reward增益，鼓励高效的局部优化而非全局打乱
- 聚合组内所有两两偏好得到结构感知的相对优势，通过tanh做非线性变换过滤极端样本影响，降低梯度方差
- 采用动作级（每个位置的排序决策）而非序列级的策略更新，细化梯度信号，进一步提升优化效率
### 关键实验
在三类场景验证效果：① LTR基准数据集（Istella、Yahoo、MSLR）；② LLM文本重排任务；③ 公平性多目标优化场景，对比LambdaRank、GRPO、PPG等基线：
- LTR场景下，SRPO在Istella数据集NDCG@10比GRPO最高提升0.24个百分点，所有指标显著优于最优监督基线，且仅需G=8的小采样组即可达到最优效果，采样效率比GRPO提升8倍
- LLM重排场景下，SRPO在BEIR跨域数据集平均NDCG@10比GRPO提升1.62个百分点，解决了常规RL排序泛化性下降的问题
- 噪声鲁棒性测试中，奖励噪声std=0.6时SRPO的NDCG@10仍比GRPO高0.7个百分点
### 核心结论
RL排序优化不能仅对标量reward做归一化，结合排序结构差异计算优势信号才能同时兼顾效果、训练稳定性和跨域泛化性
