---
title: 'nanoMuse: An Open-Source Personal Agent for Every Device You Own'
title_zh: nanoMuse：面向多设备的开源个人Agent实现
authors:
- Guangyi Liu
- Yong Liu
- Jiangning Zhang
affiliations:
- Zhejiang University
arxiv_id: '2610.08699'
url: https://arxiv.org/abs/2610.08699
pdf_url: https://arxiv.org/pdf/2610.08699
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 端侧个人Agent · 跨设备协同
tags:
- Personal Agent
- On-Device AI
- Cross-Device Collaboration
- GUI Agent
- Open Source
one_liner: 开源可跨设备端侧运行的个人Agent系统，对标Meta闭源Muse，支持本地屏幕操作
practical_value: '- Sentinel权限管控架构可直接复用：将Agent逻辑与工具调用审批逻辑解耦，按风险等级（支付、消息发送、数据导出等）做分级授权，适合电商代下单、自动客服等场景，大幅降低误操作风险

  - 跨设备peer架构可迁移：无需中心服务器运行Agent核心逻辑，每个设备端独立部署、仅同步必要会话数据，适合做覆盖用户手机、PC、线下终端的全渠道购物助理，避免用户隐私数据上传中心

  - GUI Agent混合调用策略可落地：优先调用API/命令行/浏览器能力，失败再fallback到屏幕视觉操作，大幅降低电商App自动操作的适配成本和延迟

  - 明文记忆设计可参考：将Agent记忆存储为用户可直接编辑的Markdown文件，支持操作溯源，符合电商场景用户对偏好、订单记录的可控需求，也降低Agent错误排查成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Meta 2026年推出的Muse是首款落地的个人Agent产品，但完全闭源、仅运行在Meta云服务器，用户无法掌控数据、也不能操作手机本地App，存在隐私风险和能力短板，业界缺乏可自主部署、完全开源的对等方案。

### 方法关键点
- 架构：端侧优先的peer架构，每个设备（Android/PC/Web）独立运行完整Agent、自带Sentinel权限管控模块，可选轻量中继实现跨设备会话同步，无中心依赖也可单设备运行
- 安全：Sentinel模块对所有工具调用做分级审批，支持单次/会话/永久三级授权，敏感操作（支付、发送、删除）强制单次审批，读取隐私数据后所有对外请求自动触发审批
- 操作能力：混合调用链优先用API/命令行/浏览器操作，失败后 fallback 到Hands屏幕操作模块，通过视觉+accessibility树识别界面元素，操作前输出自然语言动作说明供审核
- 记忆：所有记忆以明文Markdown文件存储，支持用户直接编辑、溯源，记忆召回支持关键词+语义向量匹配

### 关键结果数字
Android安装包仅38MB，桌面端安装后约900MB，idle内存占用0.5GB；自托管中继仅需1vCPU/1GB内存的服务器，月成本30-60元人民币；模型调用成本仅几分钱每天。对比Muse，新增Android端本地屏幕操作能力，完全开源，支持用户自选LLM供应商，也可对接私有部署模型。

### 最值得记住的一句话
个人Agent的核心不是模型能力，而是归属权——完全属于用户、可被用户掌控、能运行在用户自有设备的Agent，才是真正的个人Agent。
