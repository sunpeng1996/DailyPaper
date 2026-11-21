---
title: Online Mistake Detection in Instruction-Conditioned Procedural Video
title_zh: 指令条件下的流程类视频在线错误检测
authors:
- Amit Feldman
- Ilan Shimshoni
- Rotem Dror
affiliations:
- University of Haifa
arxiv_id: '2611.25567'
url: https://arxiv.org/abs/2611.25567
pdf_url: https://arxiv.org/pdf/2611.25567
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 多模态视频理解 · 流程任务在线错误检测
tags:
- Multimodal
- Video Understanding
- Error Detection
- Egocentric Video
- Dataset Construction
one_liner: 面向第一视角流程类视频提出指令感知的在线错误检测方案，对比两类架构性能，重划分EgoPER数据集
practical_value: '- 电商直播合规、用户上传教程类内容质检场景可复用「指令+流式内容」联合检测思路，实现实时审核替代纯离线方案

  - 模块化pipeline vs 端到端联合模型的对比结论可直接复用：短链路任务优先选联合模型避免误差传播，长链路可拆模块迭代

  - 流程类Agent（如导购指导用户组装商品、客服引导用户操作）可复用该在线错误检测框架，实时提示用户操作偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流程类视频错误检测方案存在能力短板：在线检测方法不利用指令文本，指令感知方法仅支持离线处理，无法满足实时纠错的业务需求。
### 方法关键点
聚焦第一视角流式视频的指令条件下在线错误检测任务，仅基于已观测视频片段、任务指令、历史预测结果，即可完成操作识别、时序定位，将操作分为正确、修改、疏漏、纠正、额外操作5类，遗漏步骤待视频结束后补判。对比两类架构：1）模块化pipeline，拆分步骤识别、时序定位、执行校验三个独立模块；2）联合模型，单步输出所有预测结果。重划分EgoPER数据集，所有拆分均包含错误样本支撑监督学习。
### 关键结果数字
两款方案步骤分割F1@0.5接近（93.6% vs 92.1%）；联合模型的二分类错误检测F1@0.5达84.1%，比模块化方案高3.4个百分点，其中疏漏类错误检测F1提升最显著（56.4% vs 37.5%）；模块化方案性能损失主要来自阶段间误差传播，两款方案均优于AEM、ESTANet基线。
