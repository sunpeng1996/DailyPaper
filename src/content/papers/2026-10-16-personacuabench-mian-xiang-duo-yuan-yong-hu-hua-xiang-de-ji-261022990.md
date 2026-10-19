---
title: 'PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas'
title_zh: PersonaCUABench：面向多元用户画像的计算机操作Agent评测基准
authors:
- Haoming Li
- Defu Cao
- Xu Hu
- Yingtao Luo
- Yiyang Wang
- Xianghe Xu
- Jiashu He
- Wanting Jiang
- Yifan Zhang
- Yunhan Zhao
affiliations:
- Massachusetts Institute of Technology
- Harvard University
- The University of Texas at Dallas
- University of Southern California
- Carnegie Mellon University
arxiv_id: '2610.22990'
url: https://arxiv.org/abs/2610.22990
pdf_url: https://arxiv.org/pdf/2610.22990
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent评测 · 用户画像对齐
tags:
- Computer-Use Agent
- Persona Alignment
- Benchmark
- User Satisfaction
- Task Completion
one_liner: 提出首个仅改变请求用户画像的CUA评测基准，验证真实用户请求下性能大幅下降
practical_value: '- 做电商导购Agent、智能客服Agent时，不能仅用固定任务完成率做核心评估指标，必须加入用户分层（专家/老年/年轻/务实）的满意度指标，避免出现任务完成但用户不满的体验问题

  - 可复用论文提出的「需求三标签法」（用户是否提出/Agent是否响应/是否满足）定位Agent服务故障根因，快速迭代用户需求对齐能力

  - 验证了仅给Agent透传用户profile、强制先提问再行动两种常见手段都无法解决个性化请求的性能下降问题，核心瓶颈是长任务链中用户需求的持续对齐，无需在无效干预上浪费研发资源

  - 电商场景做个性化请求理解时，可参考论文的4类用户画像分组做prompt优化，针对不同群体的表达特征适配意图识别模型，降低请求理解误差'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有计算机操作Agent（CUA）评测全部基于固定任务指令，忽略了真实用户会隐去核心需求、新增个性化约束、要求高风险操作前人工确认的特点，完成预设任务不等于满足用户真实诉求，此前没有基准可衡量同一任务下不同用户发起请求时的Agent服务效果。

### 方法关键点
- 基准覆盖11个领域共74个公开任务，包含信息查询、操作类两大类型，覆盖生活、工作两大场景；设计4类通用用户分组（专家/老年/年轻/务实），每个领域对应4个细化画像，共44个带37维属性的标准化用户画像
- 评测采用三阶段流程：1）画像Agent基于用户属性改写原始任务指令，CUA仅能看到改写后的自然请求，无法获取原始任务和用户profile；2）CUA可与画像Agent交互澄清问题，在浏览器环境执行操作；3）同时输出固定任务完成率、用户满意度两个核心指标，每个需求标注「是否被用户提出/是否被Agent响应/是否被满足」三类标签定位损失来源
- 控制变量测试9款主流CUA backbone，同时验证「给CUA透传完整用户profile」「强制CUA先提问再行动」两种常见优化手段的效果

### 关键结果
- 相比原始固定指令，个性化用户请求下9款模型平均任务完成率从0.689降至0.441，相对下降36%；其中老年用户请求下的完成率相对下降达42%
- 任务完全完成的请求中，仅62.7%能拿到用户5星好评，远低于原始指令场景的84.1%；11.2%的任务失败是因为Agent执行了用户要求的提前终止，被固定任务指标误判为失败
- 损失来源拆解：59.9%是Agent拿到明确需求后执行错误，17.1%是用户未明确提出隐性需求；仅透传用户profile、强制提问两种干预手段都无法弥补性能损失

> 最值得记住的一句话：计算机操作Agent的核心目标是服务提出请求的人，而非完成预设的固定任务
