---
title: 'ReCast: Contract-Preserving Protection for Fixed-Interface Multimodal Reasoning'
title_zh: ReCast：面向固定接口多模态推理的契约保留隐私保护框架
authors:
- Bingchen Pei
- Lichong Chen
- Bingxi Zhao
- Ziang Wu
- Sirui Wang
- Min Zhang
- Yanhao Chen
- Qingxu Liu
- Qiang Gao
- Chang-Tien Lu
affiliations:
- Beijing Jiaotong University
- Virginia Polytechnic Institute and State University
arxiv_id: '2610.01184'
url: https://arxiv.org/abs/2610.01184
pdf_url: https://arxiv.org/pdf/2610.01184
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 多模态推理隐私保护 · Agent插件框架
tags:
- Multimodal Reasoning
- Privacy Protection
- Agent Framework
- Local-Remote Collaboration
- QLoRA
one_liner: 面向固定多模态接口的Agent隐私保护框架，保92%推理精度的同时泄露率仅7.95%
practical_value: '- 可复用「多模态输入→统一文本中间表示→生成目标模态」架构，适配第三方固定API接口的同时做自定义内容加工，比如电商场景将敏感销售图表转成脱敏同结构图表调用大模型分析

  - 数值映射方案可直接迁移：敏感数值做局部可逆、保留相对关系的映射，大模型返回计算逻辑后本地替换回原数值执行，既复用大模型推理能力又不泄露核心数据

  - 小模型蒸馏方案可借鉴：用大模型生成改写样本，QLoRA微调小尺寸本地模型做隐私相关改写任务，兼顾成本、效果和隐私性

  - 生成-校验-修复的模态重建Agent流可复用，确保生成的多模态内容符合任务要求，避免格式或内容错误导致下游精度下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
调用远程多模态大模型处理图表、语音类私密数据（如企业经营报表、用户服务录音）时，直接传输原始内容存在敏感信息泄露风险；纯文本脱敏方案无法适配要求固定媒体输入的服务接口，现有模态层面隐私保护方法仍会暴露核心任务内容，同时无法保证数值推理结果的可恢复性，亟需同时满足接口兼容、隐私保护、推理精度的方案。

### 方法关键点
- 三层流水线架构：多模态证据采集模块将图像、语音、文本输入统一转换为标准化的文本证据-查询中间表示，各模块可独立插拔替换
- 联合改写层用QLoRA微调4B本地模型做语义改写，统一替换实体、主题的同时保留任务逻辑；请求级角色感知数值映射保留数值相对关系，逆映射仅存本地不对外传输
- 模态重建Agent通过生成-校验-修复闭环，将脱敏文本转换为接口要求的原模态内容，本地校验一致性后再发送到远程服务
- 远程模型返回带标记保护操作数的计算程序，本地通过逆映射替换数值后执行得到最终结果

### 关键结果
在4000条ChartQA、NMSQA测试样本上：整体精度达75.10%，保留了无保护远程推理92.43%的精度，远超所有本地基线；源内容泄露率仅7.95%，比通用文本匿名方案低一个数量级；图表模态重建比直接传输脱敏文本精度高0.4个百分点。

### 核心结论
将敏感内容的本地预处理和远程大模型的推理能力解耦，用统一文本中间表示兼容多模态输入和固定接口要求，是兼顾隐私、精度、兼容性的可行路径
