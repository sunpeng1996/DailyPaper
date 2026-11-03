---
title: 'Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights'
title_zh: 基于辅助监督的广告排序模型优化：技术与实践洞察
authors:
- Nikhil Bhale
- Apurva Pathak
- SaiSujithKumarReddy MarapaReddy
- Xiao Yin
- Prateek Bhansali
affiliations:
- Meta Platforms
arxiv_id: '2611.01280'
url: https://arxiv.org/abs/2611.01280
pdf_url: https://arxiv.org/pdf/2611.01280
published: '2026-10-31'
collected: '2026-11-03'
category: RecSys
direction: 广告CVR预测 · 多任务辅助监督
tags:
- Ads Ranking
- CVR Prediction
- Multi-Task Learning
- Auxiliary Supervision
- Noisy Label Processing
one_liner: 提出线性化标签、拆分架构、LaCo等四类辅助监督优化技术，提升广告CVR预测精度
practical_value: '- 缺CVR标签时可直接复用四类辅助信号：行为信号（加购、dwell time等漏斗行为）、语义信号（类目匹配、URL转化关键词）、特权特征训练的proxy标签、跨域合成信号，快速缓解数据稀疏问题

  - 辅助标签处理可直接复用两个trick：连续信号（如dwell time）用2-4分位桶做线性化多分类标签，比直接做回归/二分类效果更好；缺失辅助标签的样本用gating机制跳过训练，不要填0引入噪声

  - 多辅助标签降噪可直接落地LaCo方法：以主标签为基准调F-beta（优先高precision，beta建议<0.1），穷举信号逻辑组合选最优单衍生标签，避免多任务负迁移，单方案即可带来0.25%的NE提升

  - 长周期CVR预测可直接用拆分架构：拆分为多个互斥短周期子任务，预测结果求和等价于原任务，叠加主任务预测做集成可进一步提升效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
广告排序核心依赖CVR预测，但转化标签天然稀疏（仅少量点击产生转化），叠加用户隐私限制、归因困难等问题，传统仅基于转化标签的模型学习效果受限。现有多任务研究多聚焦参数共享机制优化，较少关注辅助信号的选择、处理与降噪，存在明确优化空间。

### 方法关键点
- 辅助信号体系：梳理四类可复用辅助标签来源：用户行为信号（dwell time、加购等漏斗行为）、语义信号（类目匹配、URL转化关键词匹配）、特权特征训练的proxy标签、跨域合成信号
- 架构优化：① 线性化标签：连续/序贯信号用2-4分位桶转为多分类标签，粒度优于二分类/回归；② 拆分架构：长周期CVR拆分为互斥短周期子任务，结果求和等价于原任务，再与主任务预测集成；③ gating机制：缺失辅助标签的样本跳过对应任务训练，避免填0引入噪声
- 降噪方案：① LaCo方法：以主标签为基准计算F-beta（优先高precision，beta取0.02最优），穷举信号逻辑组合选最优单衍生标签，减少多任务负迁移；② 搭配DivideMix、Tri-Training等带噪标签训练方法提升鲁棒性

### 关键结果
基线为Meta生产环境共享底层多任务pCVR模型，训练覆盖数十亿级日活点击样本，50%样本缺失转化标签，评估指标为Normalized Entropy（NE越低越好）。各技术相对基线NE提升：线性化标签-0.15%，拆分架构-0.13%，LaCo-0.25%（单方案最高增益），带噪标签训练-0.10%；全量技术上线后A/B测试广告转化量显著提升。

### 核心结论
辅助标签的质量（precision）远重于覆盖度（recall），优先选择与主目标强相关的高precision信号，效果远好于盲目增加多任务数量
