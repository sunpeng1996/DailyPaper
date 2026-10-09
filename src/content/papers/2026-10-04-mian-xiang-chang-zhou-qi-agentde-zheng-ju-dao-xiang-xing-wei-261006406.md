---
title: What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon
  Agents
title_zh: 面向长周期Agent的证据导向行为监督框架
authors:
- Zhongxiang Sun
- Jiahao Yan
- Hongkang Zhao
- Haojie Ding
- Boheng Zhang
- Fan Yang
- Xiao Zhang
- Jun Xu
affiliations:
- Renmin University of China
- Kuaishou Technology
arxiv_id: '2610.06406'
url: https://arxiv.org/abs/2610.06406
pdf_url: https://arxiv.org/pdf/2610.06406
published: '2026-10-04'
collected: '2026-10-09'
category: Agent
direction: 长周期Agent · 证据导向监督
tags:
- Long-Horizon Agent
- Agent Oversight
- Evidence Graph
- Benchmark
- Training-free
one_liner: 提出AgentMonBench评测集与无训练EBG框架，提升长周期Agent高风险决策识别与证据定位效率
practical_value: '- 可复用EBG的训练-free证据组织思路，给电商Agent（如智能客服、运营自动化Agent）做行为审计，无需额外微调即可定位高风险决策的支撑证据，降低幻觉风险

  - AgentMonBench的三类评测子集设计可迁移到内部业务Agent评测：分别覆盖需求对齐度、静默语义偏差、用户反馈回溯三个维度，补全现有Agent评测只看结果不看过程的缺口

  - 长上下文场景下的证据关联方法可直接用到推荐系统的全链路归因：将用户行为、召回排序策略、业务结果按Scope分组关联，快速定位策略迭代的实际影响，避免长日志下的信息遗漏

  - 决策优先级标注逻辑可复用：给Agent自动生成的决策打criticality标签，仅把高风险决策推送给人工审核，大幅降低长周期任务下的人工监督成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期Agent在代码开发、科研自动化、电商运营等场景落地时，用户角色已从直接决策转向执行监督，但Agent行为链路长、支撑证据分散在交互日志、工具返回结果、中间产物中，现有方案仅关注最终执行结果，无法高效定位可能影响业务目标的高风险决策，人工核验成本极高。

### 方法关键点
- 构建AgentMonBench评测集，覆盖三类核心监督场景：SpecGAP评测需求不完整时的决策对齐度，SilentSwap评测不影响现有测试通过的静默语义偏差，FeedbackTrace评测用户反馈前的高风险决策回溯能力，所有标注经双轮人工审核，一致性达92%以上。
- 提出训练-free的Evidence-Grounded Behavior Graph（EBG）框架：先抽取带源位置的证据单元，按「条件-操作-结果」（代码仓库场景）/「需求-动作-响应」（交互轨迹场景）组装为行为节点，再按上下文关联为带Scope的行为图，最终生成面向任务的轻量化证据视图，供监督模型/人工核验。

### 关键结果
在8款主流LLM（GPT-5.6系列、Claude Sonnet 5、DeepSeek V4等）上测试，对比原始上下文、RepoGraph基线：
- EBG在决策识别、证据定位两个核心任务上平均提升10%~20%，高输入长度场景增益更显著，长上下文组的证据命中率最高提升10.8%。
- 集成到Codex Harness的5个真实科研任务测试中，无EBG时未披露任何高风险决策，加EBG后100%识别并披露了需人工核验的关键问题。

### 核心结论
长周期Agent的可信性不能仅靠最终结果验证，结构化的过程证据关联是降低人工监督成本、规避静默业务风险的核心手段。
