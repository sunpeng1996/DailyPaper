---
title: Computer-Use Agents Are Embodied Generalists
title_zh: 计算机操作Agent可作为具身通用智能体
authors:
- Pranjal Aggarwal
- Sean Welleck
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.09847'
url: https://arxiv.org/abs/2611.09847
pdf_url: https://arxiv.org/pdf/2611.09847
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: 具身Agent · 通用计算机操作Agent复用
tags:
- Computer-Use Agent
- Embodied AI
- Generalist Agent
- GUI Interaction
- Reinforcement Learning
one_liner: 将具身任务封装为软件交互，单款计算机操作Agent无定制调优就在4项ECCV具身竞赛获奖
practical_value: '- 开发跨场景通用Agent时，可参考「核心Agent固定+场景适配层改为GUI/软件封装」的架构，减少不同场景下的模型重复调优成本，比如电商多场景（直播/详情页/客服）Agent适配可复用该思路

  - 落地多模态交互Agent时，可复用「GUI交互能力可迁移到相似多模态决策任务」的结论，现有GUI操作Agent稍作封装就能适配3D场景导购、虚拟试穿等具身交互任务

  - 搭建Agent训练环境时，可借鉴自动生成可视化标注数据的思路，用模拟器生成visual grounding监督数据，降低Agent多模态交互任务的标注成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前具身AI大多依赖任务定制的模型架构和专用接口，泛化性差、开发成本高；而计算机操作Agent（CUA）已在通用数字任务上验证了强泛化性，二者在visual grounding、环境探索、反馈迭代等核心能力上高度重合，存在能力迁移的可能性。

### 方法关键点
- 核心Agent固定为基于Gemini 3.5/3.6 Flash的CUA，统一使用截图感知、键盘/鼠标动作空间，无竞赛特定调优
- 为4类具身任务分别开发封装软件：将3D导航、对话导航、3D分割、视频分割任务的环境渲染为GUI界面，把物理/3D环境操作映射为键鼠操作
- 交互逻辑：Agent接收任务描述+界面截图，根据历史交互输出键鼠动作，软件执行后返回新截图，循环到提交结果；上下文满20张截图时删除最早10张，保留完整参考视频

### 关键实验
- 评估基准为4项ECCV 2026具身AI竞赛：VLNVerse导航、DialNav对话导航、OpenSUN3D 3D分割、MeViSv2视频分割，对比所有参赛定制化方案
- 核心结果：单款CUA无任务调优，获OpenSUN3D第1（AP50 25.88，领先第二名4.43）、MeViSv2-Text第2（Final 86.72）、DialNav第3、VLNVerse第6；GUI交互与API交互的性能差控制在4分以内，2项任务GUI表现更优；无专用动作头的9B VLM在机器人任务上达到与π0.5相当的成功率（56% vs 59%）

### 核心结论
具身AI完全可以复用计算机操作Agent的发展路径，通过visual grounding预训练、RL环境规模化、实时交互优化三步走向单模型通用化
