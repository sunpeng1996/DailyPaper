---
title: Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender
  Systems with Collaborative Agents
title_zh: 基于协作多Agent的黑盒推荐系统可控性评估框架CtrlBench-Rec
authors:
- Jiwen Zhou
- Xiang Liu
- Mingming Li
- Pengbo Mo
- Jiao Dai
- Honglei Lv
- Jizhong Han
- Songlin Hu
affiliations:
- 中国科学院信息工程研究所
- 中国科学院大学网络空间安全学院
arxiv_id: '2607.13418'
url: https://arxiv.org/abs/2607.13418
pdf_url: https://arxiv.org/pdf/2607.13418
published: '2026-07-15'
collected: '2026-07-16'
category: Eval
direction: 多Agent协作 · 推荐系统可控性评估
tags:
- Multi-Agent
- Recommender System
- Controllability
- Evaluation
- Black-Box
- LLM Agent
one_liner: 提出首个多Agent黑盒推荐可控性评估框架，覆盖三类任务，可量化可控性并暴露系统瓶颈
practical_value: '- 可复用CtrlBench-Rec的三层可控性评估任务（目标内容发现/兴趣画像塑造/流行度偏差缓解），作为自家推荐系统迭代后的合规性、可干预性评测标准，替代零散人工测试。

  - Agent冷启动对齐的「注册-搜索-点击」三步流程、仅需4-6条初始交互行为即可完成系统识别的结论，可直接复用在推荐系统仿真探针、用户模拟Agent开发中，大幅降低冷启动数据成本。

  - 多Agent进化融合思路（BERT编码行为+KMeans聚类+群体讨论生成超级探针）可迁移到黑盒推荐系统的攻击测试、漏洞挖掘场景，用更少探针覆盖更多边界Case。

  - 实测得到的「黑盒推荐系统对长尾内容引导存在天然抵抗、可控内容占比上限约55%」的结论，可作为可控推荐算法迭代的基准参考线，明确优化天花板。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统作为黑盒，用户/监管方无法干预输出、审计行为，传统评估仅关注准确率、公平性等静态指标，缺少动态交互的可控性（系统响应显式引导的能力）量化框架，单Agent探索成本高、效率低，无法适配多样控制目标。

### 方法关键点
- 定义三层递进式可控性评估任务：目标内容发现（测试显式指令响应能力）、兴趣画像塑造（测试隐式用户表示引导能力）、流行度偏差缓解（测试算法偏见纠正能力）
- 提出进化式多Agent框架CtrlBench-Rec：先基于真实用户数据初始化Agent群体，经过冷启动对齐（注册-搜索-点击同步系统侧用户索引）、多轮交互，再通过BERT编码Agent行为、KMeans聚类、群体讨论融合生成少量高能力超级探针，大幅降低交互成本
- 全程仅需黑盒访问，无需获取推荐系统内部参数，适配所有主流推荐架构

### 关键结果数字
实验基于MovieLens-1M、Amazon Toys & Games两个公开数据集，对比100个随机Agent的Base-Large、26个随机Agent的Base-Small、仅聚类选优的KMeans-Fusion三类基线：
1. 相同Agent数量下，CtrlBench-Rec的目标内容覆盖率比Base-Small最高高80%，探索效率提升40%；
2. 仅用26个超级探针即可达到接近100个随机Agent的覆盖效果，交互成本降低74%；
3. 黑盒推荐系统的可控内容占比天然存在约55%的上限，长尾内容引导存在强抵抗，中等流行度内容因语义分散存在引导陷阱。

**最值得记住的一句话**：仅靠外部引导无法突破黑盒推荐系统的长尾内容曝光瓶颈，可控性优化需要从模型底层架构入手。
