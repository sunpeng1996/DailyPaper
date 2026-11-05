---
title: 'From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao
  Feed Recommendation'
title_zh: 淘宝Feed推荐高分未曝光候选回收系统URED落地实践
authors:
- Ge Fan
- Kai Meng
- Huiping Chu
- Yuning Jiang
- Han Zhu
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2611.05997'
url: https://arxiv.org/abs/2611.05997
pdf_url: https://arxiv.org/pdf/2611.05997
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 工业推荐 · 召回层发现性优化
tags:
- Recall
- Exploration-Exploitation
- Industrial Recommendation
- Filter Bubble
- Cold Start
one_liner: 无需训练的召回层方案URED，回收排序高分未曝光候选，提升推荐发现性同时保留用户engagement
practical_value: '- 可直接复用URED的无训练设计：在现有推荐流水线新增召回通道，异步存储30天窗口内排序高分未曝光候选，仅增加<1%延迟，无需修改排序逻辑、重训模型，落地成本极低

  - 先做ranker校准审计再做探索优化：不要直接暴力注入冷探索候选，先统计冷内容的PCOC（预测/实际点击比）和RMSE，避免盲目提探索反而损伤engagement

  - 超参数可先离线筛选再做AB实验：通过DAU覆盖率、用户候选池长度两个离线指标快速定位聚合窗口、每请求注入配额的最优区间，节省AB测试预算

  - 面向业务做可配置发现规则：自定义发现性判定阈值（如用户多少天未曝光的类目），配套后台看板方便产品/运营调参，加速跨团队对齐和上线审批'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐过度优化短期engagement导致过滤泡严重，用户新兴趣发现不足；现有方案要么是多目标/RL/LLM类方法，训练推理成本高，要么是暴力注入冷探索候选，会因ranker对冷候选系统性高估，不仅发现性提升有限还损伤engagement，亟需低成本、无负向影响的探索方案。

### 方法关键点
- 核心洞察：排序阶段打分高但因位置/竞争未曝光的候选，同时具备高相关性和预测可靠性，是工业流水线普遍被丢弃的优质资源
- 轻量流水线设计：1）摄入：每次排序后保留Top200高分未曝光候选异步落HDFS；2）聚合：天级任务按用户聚合30天滑动窗口内的未曝光候选，去重后保留Top10000/用户；3）挖掘：过滤出用户过去15天未曝光类目的候选；4）在线serving：候选存Redis，作为独立召回通道每请求最多返回1000个候选，O(1)查找，无需模型重训

### 关键实验
淘宝千万级DAU feed场景线上AB实验，对比基线流水线：核心指标发现类目+3.47%，内容丰富度+8.47%，完播VV+2.62%，总VV+0.36%（不显著），延迟 overhead <1%；消融实验显示1天聚合窗口仅保留16%发现性收益，随机注入冷候选无显著发现性收益且总VV降0.17%；通道对比显示URED发现率85.9%，是平台平均的13.9倍、最强近线召回基线的6.3倍，有效播放率达平台平均的1.03倍。

> 最值得记住的结论：探索的engagement损失不是固有trade-off，而是注入了模型无法保证置信度的候选导致的，工业流水线丢弃的高分未曝光候选是极低投入的优质探索资源。
