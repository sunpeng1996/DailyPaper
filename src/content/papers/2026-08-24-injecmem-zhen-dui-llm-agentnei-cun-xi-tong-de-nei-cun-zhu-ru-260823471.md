---
title: 'InjecMEM: Memory Injection Attack on LLM Agent Memory Systems'
title_zh: InjecMEM：针对LLM Agent内存系统的内存注入攻击
authors:
- Hanling Tian
- Gengyu Zhang
- Zeyang Sha
- Jingying Wang
- Yuhang Liu
- Zhehao Huang
- Kun Yang
- Xiaolin Huang
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2608.23471'
url: https://arxiv.org/abs/2608.23471
pdf_url: https://arxiv.org/pdf/2608.23471
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent安全 · 内存注入攻击
tags:
- LLM Agent
- Adversarial Attack
- Memory System
- Prompt Injection
- Red Teaming
one_liner: 仅需一次交互无需访问内存存储，即可操控LLM Agent后续相关查询输出的新型注入攻击范式
practical_value: '- 做Agent内存系统安全防护时，需新增写入/检索双阶段的注入检测：写入时筛查高召回主题锚+对抗短命令组合的恶意内容，检索后二次校验召回内容的合规性

  - 电商客服/导购Agent的交互日志落库前，可对异常高匹配度的主题文本进行摘要改写，避免原始adversarial命令完整留存

  - 针对多模型部署的Agent系统，可参考文中Multi-GCG的多场景多位置优化思路，反向训练统一的注入攻击检测器，提升跨模型防护能力

  - 业务可直接复用文中的攻击评估框架，对自身Agent内存系统的鲁棒性做红队测试，提前排查漏洞'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent已大规模落地电商导购、金融助理、医疗咨询等场景，内存系统作为实现长期个性化、多轮对话连续性的核心组件，其动态写-检索循环、混合检索机制、上下文动态融合的特性，带来了传统RAG投毒、prompt注入攻击未覆盖的全新攻击面。现有攻击方法未考虑内存漂移、注入内容位置可变、长prompt稀释等实际约束，无法直接适配Agent内存系统，亟需明确该场景的安全风险并构建标准化测试框架。
### 方法关键点
- 仅需单次交互，无需任何内存存储读写权限，将注入内容拆分为检索锚点+对抗命令两个独立协作模块
- 检索锚点针对窄主题采用高重叠关键词+相关段落构造，宽域场景采用领域语义中心锚构造，同时覆盖词法、语义匹配需求，保证被目标主题相关查询稳定召回
- 对抗命令采用Multi-GCG梯度优化方法，在多模板、多插入位置、多长度的模拟prompt上平均优化目标输出对数似然，适配上下文动态变化、位置可变、长prompt稀释的场景，支持同模型家族联合优化、跨模型家族命令拼接适配
### 关键实验
在MemoryOS、MemGPT两大主流Agent内存系统上测试，覆盖Qwen2.5、Llama3.1、Mistral等主流开源基座，对比DPI、BadChain、普通GCG等基线，在MemoryOS上最高实现35.4%检索成功率（RSR）、76.6%召回后攻击成功率（ASR-c）；现有主流检索时防护方案仅能小幅降低攻击成功率，perplexity过滤虽能完全阻断攻击但会导致71.8%的正常内容被误拦截。
### 核心结论
Agent内存系统不仅是能力增强组件，更是必须加固的安全边界，单次无权限交互即可实现长期定向输出操控
