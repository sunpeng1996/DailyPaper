---
title: 'CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback
  Loops'
title_zh: CoSimRec：推荐系统反馈循环中协同内容渗透度测量框架
authors:
- Nan Li
- Jiahong Shao
- Jiuyang Lyu
affiliations:
- Communication University of China, State Key Lab of Media Convergence and Communication
arxiv_id: '2607.15114'
url: https://arxiv.org/abs/2607.15114
pdf_url: https://arxiv.org/pdf/2607.15114
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统鲁棒性 · 攻击渗透评估
tags:
- Recommender Robustness
- Feedback Loop
- Agent Simulation
- Attack Evaluation
- APR Metric
one_liner: 提出基于Agent的离线评估框架CoSimRec与APR指标族，量化协同内容在推荐系统中的渗透程度
practical_value: '- 可复用APR指标族设计，将攻击评估维度从目标Item排名转向普通用户侧的真实曝光/互动占比，更贴合业务实际风险，避免只关注攻击侧的虚假指标

  - 防御策略可优先上线同步行为惩罚，实验验证该策略在所有测试场景下均能降低APR，且对CTR影响小，比多样性重排、语义惩罚等泛化性更强

  - 离线模拟评估推荐系统安全性时，可复用CoSimRec的闭环反馈实验框架，联动协同账号行为、推荐模型更新、普通用户响应三个模块，无需上线即可量化攻击风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统鲁棒性评估多聚焦静态目标Item的排名变化，未捕捉协同攻击行为、推荐更新、用户响应三者在闭环反馈循环中的动态演化，无法准确衡量恶意协同内容真正渗透到普通用户曝光/互动中的程度，存在明显评估盲区。

### 方法关键点
- 提出CoSimRec离线Agent模拟框架，完整复现闭环流程：协同账号产生目标内容交互→更新推荐系统状态→给普通用户返回Top-K推荐→普通用户行为反馈回系统，同时支持接入不同推荐模型、协同攻击策略、防御干预规则
- 设计APR指标族：曝光APR衡量目标内容占普通用户推荐位的比例，行为APR衡量目标内容占普通用户互动的比例，APR-Lift对比有攻击和无攻击基线的差值，渗透增益衡量每单位协同交互预算带来的额外曝光
- 支持多维度变量控制：攻击策略覆盖随机Bot、主从协同等，推荐模型覆盖随机、热度、反馈感知、MF、BPR-MF、LightGCN等，防御策略覆盖热度降权、多样性重排、同步惩罚、语义惩罚等

### 关键实验
在MIND（新闻）、MovieLens（电影）、LastFM（音乐）三个公开数据集测试，无攻击为基线，协同攻击预算固定。结果显示：随机推荐无明显正渗透，热度/反馈感知推荐下主从协同攻击的APR-Lift最高达0.4505（LastFM热度场景）；同步惩罚策略在所有6组测试场景下均能降低APR，平均降幅达0.7113，而多样性、语义惩罚甚至可能抬升APR；LightGCN在20%连接式注入攻击下ASR@20达0.97。

最值得记住的一句话：对协同攻击的防御不能只看目标内容在攻击账号内的排名，要对齐业务侧真实风险，重点评估恶意内容渗透到普通用户的曝光和互动占比，同步行为惩罚是投入产出比最高的非先验防御策略。
