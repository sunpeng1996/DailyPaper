---
title: 'Learning How to Remember: Memory Modality Selection for GUI Agents'
title_zh: 面向GUI Agent的动态记忆模态选择框架SwitchMem
authors:
- Taeyun Roh
- Suhyeong Park
- Gijin Kim
- Wonjune Jang
- Jaewoo Kang
affiliations:
- Korea University
- Myongji University
- AIGEN Sciences
arxiv_id: '2610.17928'
url: https://arxiv.org/abs/2610.17928
pdf_url: https://arxiv.org/pdf/2610.17928
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: GUI Agent · 多模态记忆路由优化
tags:
- GUI Agent
- Memory Routing
- Multimodal Memory
- VLM
- Dynamic Modality Selection
one_liner: 基于VLM隐藏态信号训练轻量路由，每步动态选择文本/视觉记忆模态提升GUI Agent性能
practical_value: '- 做电商导购Agent、移动端操作Agent时，可借鉴动态模态选择思路：UI元素密集、功能类操作场景优先用视觉记忆，简单导航、初始步骤场景优先用文本记忆，既能提升执行准确率，又能降低token消耗

  - 多模态RAG系统可复用该框架思路：无需固定拼接文本+图像的检索结果，针对当前query场景动态选择返回最优模态的记忆内容，比固定多模态拼接效果更好、开销更低

  - 可直接复用D-CoE方法从冻结大模型的深层隐藏态提取偏好信号，无需大量人工标注就能训练轻量路由模块，避免微调大模型的高额成本，适配业务快速迭代需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM驱动的GUI Agent记忆增强方案普遍采用固定模态设计，要么统一输出文本记忆，要么统一输出视觉记忆，忽略了不同交互步骤对记忆模态的偏好差异。文本记忆虽然紧凑，却会丢失UI界面的细粒度空间、布局信息；视觉记忆保留了完整界面信息，却在简单场景下存在冗余，会增大推理开销甚至引入干扰，固定模态始终无法取得全局最优性能。
### 方法关键点
- 提出Directional Chain-of-Embedding（D-CoE）分析方法，对比相同检索记忆分别以文本、视觉形式输入时VLM的中间隐藏态差异，发现Transformer深层隐藏态可稳定预测每步最优记忆模态，AUROC最高达0.8。
- 设计SwitchMem两阶段轻量路由框架：第一阶段基于D-CoE信号生成无标注的软偏好标签；第二阶段训练两层MLP路由，输入当前状态嵌入、记忆嵌入的拼接、点积、差特征，输出文本/视觉记忆的相对得分，每步动态选择最优模态输入给冻结的VLM，无需微调大模型。
### 关键实验
在AITW、LearnGUI、MobileMiniWoB三个主流GUI Agent基准上对比10+基线（含固定文本/视觉记忆、RAG-GUI、M3A、AppAgent等），SwitchMem分别取得51.42%、38.13%、63.04%的性能，比最优固定记忆基线分别提升2.12、0.69、2.17个百分点，推理延迟仅比固定视觉记忆高0.1~0.3s/step，远低于其他复杂记忆增强方案。

最值得记住的一句话：记忆模态选择是交互步骤级的动态决策，而非任务级的固定设计，利用大模型内部隐藏态的原生偏好信号可以极低的成本实现显著性能提升
