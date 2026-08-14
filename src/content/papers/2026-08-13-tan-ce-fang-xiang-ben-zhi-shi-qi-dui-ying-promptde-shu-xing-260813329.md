---
title: A Probe Direction Is a Property of Its Prompt
title_zh: 探测方向本质是其对应Prompt的属性
authors:
- Valentin Noël
affiliations:
- Devoteam
arxiv_id: '2608.13329'
url: https://arxiv.org/abs/2608.13329
pdf_url: https://arxiv.org/pdf/2608.13329
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 大模型评估 · 激活探测方法校准
tags:
- LLM Probing
- Activation Probe
- Evaluation Robustness
- Prompt Engineering
- Model Comparison
one_liner: 揭示LLM激活探测结果高度依赖Prompt选择，证明单Prompt设计无法支撑跨模型比较并给出可信对比所需Prompt数
practical_value: '- 做LLM4Rec/Agent效果评估时，不能依赖单Prompt测试，需覆盖多类业务场景Prompt避免结果偏倚

  - 基于模型激活的安全/对齐探测方案，必须将Prompt作为核心变量纳入设计，否则探测结果可信度极低

  - 跨LLM选型对比时，需固定统一的Prompt集合与统计规则，避免因Prompt选择差异得出错误的选型结论'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM激活探测方案通过对比含评估提示与普通提示的激活差判断模型是否感知测试，默认Prompt为固定参数，未验证其对结果的影响，导致不同研究结论矛盾。
### 方法关键点
固定任务文本仅变更「评估提示」表述，对比不同Prompt下的探测得分、模型规模相关性趋势；拆分探测得分方差来源，验证表面文本特征对结果的干扰。
### 关键结果数字
- 模型自身仅贡献探测得分方差的小部分，大部分方差来自模型与Prompt的交互，增加测试样本无法修正偏差，仅调整Prompt可复现不同研究的相反结论
- 不含任何评估信息的纯表面文本特征，可复现已发表研究中相当比例的探测得分
- 单Prompt设计完全无法支撑跨模型比较，明确给出了可信对比所需的Prompt数量要求
