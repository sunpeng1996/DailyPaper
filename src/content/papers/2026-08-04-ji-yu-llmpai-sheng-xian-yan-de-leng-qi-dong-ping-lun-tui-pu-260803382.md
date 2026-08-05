---
title: LLM-Derived Priors for Thompson Sampling in Cold-Start Comment Recommendation
title_zh: 基于LLM派生先验的冷启动评论推荐汤普森采样优化方法
authors:
- Eugene Lee
- Oseong Choi
- Byungsoo Kang
- Taeyeong Jang
affiliations:
- NAVER WEBTOON
arxiv_id: '2608.03382'
url: https://arxiv.org/abs/2608.03382
pdf_url: https://arxiv.org/pdf/2608.03382
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 冷启动推荐 · LLM赋能汤普森采样
tags:
- Thompson Sampling
- Cold Start
- LLM Prior
- Comment Recommendation
- Multi-armed Bandit
one_liner: 将LLM提取的评论语义信号转为贝叶斯先验，实现评论推荐场景汤普森采样的冷启动优化
practical_value: '- 冷启动UGC推荐场景可直接复用「离线LLM生成语义先验+在线Thompson Sampling实时更新」的架构，LLM不接在线流量，仅做离线批量计算，成本低、latency可控，可迁移到电商商品晒单推荐、短视频评论推荐等场景

  - Thompson Sampling的先验设计可参考「通用基础分+人群/场景调整分」的拆分结构，将LLM输出直接校准为类CTR的[0,1]分数，无需额外做概率映射即可快速转为Beta分布伪计数

  - 人群差异显著的推荐场景可采用分性别/年龄等粗粒度人群段维护后验的方案，既避免全用户粒度建模的数据稀疏问题，又不会因全局pooling掩盖不同人群的偏好异质性

  - 上线LLM先验的bandit策略时需权衡利用效率和曝光多样性，LLM先验会导致流量向高评分内容集中，需补充多样性/新鲜度约束避免内容生态两极分化'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
汤普森采样是在线推荐领域广泛应用的多臂老虎机算法，但新上架的UGC类内容臂（如用户评论）缺乏交互数据时会面临严重冷启动问题，而文本本身的语义信息可以在稀疏反馈阶段反映内容吸引力，现有方案很少将LLM的语义理解能力和贝叶斯先验结合实现老虎机的冷启动优化。

### 方法关键点
- 采用**离线LLM先验构造+在线分人群后验更新**的两段式架构，LLM仅在评论入库时批量完成语义打分，在线阶段每小时基于7天滑动窗口的交互数据，分性别-年龄8个细分人群段更新汤普森采样的Beta后验参数
- 先验采用通用基础分+调整分的可拆解设计：通用基础分衡量评论的普遍吸引力，校准为[0,1]类CTR值；可选两类调整项：性别调整分捕捉不同性别对评论风格的偏好差异，内容调整分衡量评论对所属内容核心特色的表达程度
- LLM输出直接校准为概率级分数，通过固定先验强度κ=40转为Beta分布的伪计数，无需额外的分数到概率的映射步骤

### 关键实验结果
在NAVER WEBTOON的评论推荐场景开展A/B/C测试，三组流量各约59.5万用户，测试周期4周，基线为Uniform Prior：
- 冷启动稀疏反馈阶段（评论累计曝光10~49次），性别先验CTR相对提升9.51%，内容先验CTR相对提升7.76%，均达p<0.001显著性
- 分人群效果差异显著：性别先验的CTR增益集中在17岁以下男性群体，最高达13.76%；内容先验整体CTR下降5.68%，但CVR相对提升1.37%，起到了精准筛选高转化用户的作用

### 最值得记住的结论
LLM无需作为在线排序器/生成器直接承接流量，作为离线语义先验赋能传统在线策略，是兼顾成本、低延迟和业务效果的可行落地范式。
