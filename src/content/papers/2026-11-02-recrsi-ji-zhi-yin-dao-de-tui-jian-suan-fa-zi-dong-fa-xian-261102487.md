---
title: 'RecRSI: Mechanism-Guided Discovery of Recommendation Algorithms'
title_zh: RecRSI：机制引导的推荐算法自动发现框架
authors:
- Tingran Gan
- Zhouziyue Lu
- Dian Jin
- Tao Li
- Yang Gao
- Ming Liu
- Weiwen Liu
- Jianghao Lin
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- Meituan
arxiv_id: '2611.02487'
url: https://arxiv.org/abs/2611.02487
pdf_url: https://arxiv.org/pdf/2611.02487
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 驱动推荐算法自动演进
tags:
- LLM Agent
- Recommender System
- Automated Algorithm Discovery
- Mechanism Guided
- Self-Evolving
one_liner: 基于机制假设的LLM驱动推荐算法自动发现框架，性能优于现有所有自动演进方案
practical_value: '- 可复用「机制假设-验证」迭代范式：将业务中推荐算法调优（如排序策略、损失函数、表征模块修改）拆解为明确的假设单元，搭配自动化实验平台，可自动生成实验优先级，大幅降低人工试错成本

  - 可迁移MechSpace的组件拆解思路：把业务推荐链路的可修改模块（表征、打分、损失、采样、更新等）拆解为可组合原语，明确兼容规则，可大幅减少无效的组合尝试，提升调优效率

  - 可复用机制反馈的沉淀逻辑：每次实验结果不仅记录指标，还要关联修改的机制、参考基线、上下文配置，沉淀的经验可直接指导后续优化方向，避免重复踩坑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前推荐算法迭代需要协调表征、打分函数、损失函数、优化流程等多个相互依赖的组件，人工试错成本高；现有自动演进方案多为代码级随机搜索，缺乏机制层面的因果关联，实验反馈复用率低，有限预算下优化效率差。
### 方法关键点
- 核心以「机制假设」为迭代单元：每个假设包含参考基线、待修改的机制组合、优化逻辑、预期效果，明确单次实验的变量与上下文，避免无意义的修改
- 三层核心架构：① MechSpace：从初始算法源码和任务接口自动抽取可落地的机制原语（覆盖表征、打分、损失、更新、架构、采样6类）与组合规则，保证生成的修改可执行；② Research Line：通过4个互补角色（机制组合、链路迭代、假设证伪、前沿探索）生成假设池，筛选可行方案落地；③ Mechanism Feedback：将实验结果与对应假设、上下文关联更新到共享状态，指导下一轮迭代
- 迭代逻辑：无论实验成败都沉淀机制层面经验，成功组合作为后续迭代基线，失败实验排除无效方向，避免重复尝试
### 关键实验
在Amazon CDs、Electronics、Office、MovieLens-1M四个公开数据集上测试，初始基准覆盖SASRec、MoRec、BERT4Rec、NGCF四类主流推荐算法，对比RecHarness、DeepEvolve等5个SOTA自动演进方案。16个模型-数据集组合下，RecRSI相对初始算法平均提升NDCG@5 8.48%、HR@5 6.88%，相对各场景最优基线平均提升NDCG@5 2.60%、HR@5 2.20%，GPU效率达1.96pp/h，优于所有对比方案。
### 核心结论
推荐算法自动迭代的核心不是随机代码变异，而是基于机制因果关联的假设验证，用好实验上下文反馈比单纯增加试错次数效率高得多
