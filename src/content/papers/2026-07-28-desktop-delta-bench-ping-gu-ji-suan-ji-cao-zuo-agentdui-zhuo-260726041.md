---
title: 'Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?'
title_zh: Desktop-Delta Bench：评估计算机操作Agent对桌面GUI状态转换的理解能力
authors:
- Abhishek Pillai
- Samir Kumar Nayak
- Yuan Chen
affiliations:
- NVIDIA
arxiv_id: '2607.26041'
url: https://arxiv.org/abs/2607.26041
pdf_url: https://arxiv.org/pdf/2607.26041
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 桌面GUI操作能力评测
tags:
- Computer-Use Agent
- VLM
- GUI Benchmark
- State Transition
- Temporal Ordering
one_liner: 提出面向桌面GUI状态转换的离线评测基准DDB，定位计算机操作Agent的中间推理缺陷
practical_value: '- 做桌面自动化Agent（如电商运营自动化、店铺后台操作Agent）的团队，可直接用DDB的2类任务设计做内部VLM选型，优先测试时序排序和动作重构能力，比端到端测试成本低

  - 可借鉴DDB的decoy注入设计，在自有Agent评测中加入无效上下文干扰项，提前定位上下文中毒风险，适配电商后台多窗口切换等易混淆场景

  - 开发GUI交互Agent的动作预测模块时，可优先优化drag、key_command类动作识别，当前VLM在这两类的F1比click低20-40pct，是主要性能瓶颈

  - 自建GUI Agent评测集可复用DDB的标注流程：先自动采集轨迹再过滤歧义样本，63%左右的标注保留率可作为质量控制参考'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）的评测多聚焦端到端任务成功率或单帧GUI grounding，无法定位模型对动作引发的状态转换的理解缺陷；而桌面环境异步性强，易出现延迟、遮挡、无关窗口等干扰，导致Agent误判进度、上下文中毒，甚至盲目执行错误操作，亟需细粒度的过渡层评测基准。

### 方法关键点
- 设计2类互补评测任务：① 三帧时序排序：含105组带跨轨迹干扰的decoy样本，模型需还原时序并识别无关帧；② 单动作重构：1550组动作前后帧对，需预测click/drag/scroll/text_entry/key_command共5类动作及对应的结构化payload
- 数据覆盖Linux桌面15+办公应用、50个任务域，所有2013个样本均经过人工校验，针对状态验证、来源跟踪、上下文感知控制3类核心失败维度设计
- 评测无需运行VM，完全离线执行，可单独拆解动作类别识别、空间定位、payload还原等细分能力的缺陷

### 关键结果
评测8款主流闭源/开源VLM，时序排序任务最优精确匹配率仅65.1%（无decoy）/65.7%（有decoy），远未饱和；加入任务上下文可提升decoy识别率6.9pct，但会降低无decoy排序准确率2.2pct。单动作重构任务：click类F1最高达0.96，但drag类最高仅0.76，key_command payload准确率最高仅46.4%；闭源模型平均macro F1 0.768，比开源模型高21.8pct。

**最值得记住的一句话**：端到端任务成功不代表Agent中间状态理解正确，过渡层的状态转换评测是定位CUA可靠性缺陷的必要环节
