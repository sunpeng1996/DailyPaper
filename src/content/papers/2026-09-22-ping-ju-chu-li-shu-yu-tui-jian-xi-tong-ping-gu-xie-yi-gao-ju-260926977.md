---
title: 'Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit
  for Tie-Heavy Recommender Scores'
title_zh: 平局处理属于推荐系统评估协议：高平局打分的顺序不变性审计
authors:
- Chengkun Guo
- Han Chen
- Yilin Zhu
- Yingrui Li
affiliations:
- Independent Researcher (Bethlehem, PA, USA)
- Independent Researcher (Washington, DC, USA)
- Independent Researcher (Seattle, WA, USA)
arxiv_id: '2609.26977'
url: https://arxiv.org/abs/2609.26977
pdf_url: https://arxiv.org/pdf/2609.26977
published: '2026-09-22'
collected: '2026-09-24'
category: Eval
direction: 推荐系统离线评估 · 平局处理规范
tags:
- Recommender System
- Offline Evaluation
- Tie Breaking
- Reproducibility
- Sampled Metrics
one_liner: 揭示推荐离线评估平局处理规则对指标的巨大影响，给出可复现评估检查清单
practical_value: '- 离线评估时禁止默认使用正例在前的输入顺序稳定排序处理平局，改用基于user ID、item ID和固定种子的确定性hash平局打破规则，避免指标虚高

  - 针对离散特征匹配、规则类、计数类等易产生大量平局的打分组件，需做平局敏感性校验，指标降幅过大则说明得分区分度不足

  - 评估报告可复用给出的6项检查清单，覆盖候选集、预排序顺序、平局占比、平局规则、置换测试、敏感性分析，保障结果可复现'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统离线top-k评估的结果稳定性长期受未明确声明的平局处理规则影响，现有流程常默认将正样本放在候选集首位再做稳定排序，平局时正样本必然优先，导致指标虚高、实验不可复现，尤其在离散特征匹配、规则打分等易产生大量平局的场景下问题更突出，亟需明确平局处理的评估规范。
### 方法关键点
- 定义行顺序不变性：仅改变候选集输入顺序、不改变item身份/标签/得分时，最终排序和指标保持不变才是可靠评估器
- 推导单正例场景下均匀随机平局处理的Hit@k、NDCG@k精确期望公式，降低实验开销
- 对比4种平局处理方案：输入顺序平局、确定性hash平局、多次随机平局、均匀随机期望计算
- 6项评估报告检查清单可覆盖全流程平局相关参数披露要求
### 关键实验结果
在Amazon Beauty&Personal Care（3万条样本）和MovieLens 25M（1万用户）数据集测试：① 加权属性重叠打分下，Amazon NDCG@10从输入顺序的0.8474降至确定性hash的0.1702，Hit@10从0.9997降至0.3526，波动超0.67；② MovieLens标签重叠打分NDCG@10从0.838降至0.2332，波动超0.6；③ 无平局的残差属性打分、流行度打分，指标差小于0.0005；④ 多次hash种子的平均结果与理论期望高度一致。
### 核心结论
如果你的推荐模型离线指标在更换平局处理规则后大幅下降，说明模型得分区分度极低，指标虚高完全来自评估流程的隐性偏好。
