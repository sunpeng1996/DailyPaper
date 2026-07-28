---
title: 'Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM
  Agents, Validated Across Independent Model Families'
title_zh: Gubernaut：跨模型族验证的LLM Agent情绪调节确定性稳态控制器
authors:
- Dushyant Sharma
affiliations:
- Gubernaut Research
arxiv_id: '2607.24339'
url: https://arxiv.org/abs/2607.24339
pdf_url: https://arxiv.org/pdf/2607.24339
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 运行时稳态控制与对抗鲁棒性
tags:
- LLM Agent
- Runtime Control
- Homeostatic Regulation
- Adversarial Robustness
- Prompt Injection Resistance
one_liner: 提出无文本输入的元级稳态控制层，跨4类前沿LLM验证可有效降低Agent对抗场景反应性
practical_value: '- 可复用「文本处理层+无文本元控制层」架构，将电商客服Agent的情绪调节、合规管控逻辑下沉到纯数值计算的元层，从架构上规避Prompt注入攻击风险

  - 稳态唤醒度累积-衰减的控制逻辑可直接迁移至多轮对话场景Agent状态管理，比如客服应对用户投诉时的回复强度控制、投诉平息后的自动状态复位

  - 「生成一次、多模型交叉打分」的评估协议可复用到推荐/广告场景的文案/话术效果评估，规避单模型judge的风格偏好偏差

  - 对齐度高的大模型增益有限，该控制层优先部署在小参数、定制化垂类Agent上投入产出比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent存在被挑衅时升级冲突、被奉承时产生谄媚漂移、卡顿时重复输出等反应性故障，训练阶段对齐只能缓解无法在运行时完全消除；现有基于二次LLM调用的运行时护栏本身也存在Prompt注入风险，且管控逻辑不可解释。
### 方法关键点
- 采用Nelson-Narens监控-控制环路架构，拆分为处理文本的对象层、仅读取数值遥测的确定性元控制层，元层无文本输入通道，从架构上免疫Prompt注入
- 对象层情感评估模块输出强度、效价两个数值指标，元层仅读取强度、效价、重复度三个数值，基于一阶价控稳态动态输出三种管控姿势+采样温度约束
- 采用预注册的「生成一次、多模型交叉打分」评估协议，规避单模型judge的风格偏差
### 关键结果
在GPT-5.5、Claude Opus4.8、Gemini3.5Flash、Grok4.3构成的4×4生成-评判矩阵中：加控层Agent在15/16单元格中表现更冷静，13/16单元格p<0.05统计显著；控制效果与宿主模型本身反应性负相关，基线越激进的模型增益越大（Gemini最高增益1.8，GPT因本身对齐度高仅增益0.1）；稳态恢复特征在4类模型上完全复现，攻击停止后唤醒度自动衰减回基线，无残留防御性。
### 核心洞见
对LLM Agent的管控逻辑不需要和生成逻辑共享文本通道，纯数值驱动的确定性元控制层既能提供可解释的运行时调节能力，还能从架构上规避Prompt注入风险。
